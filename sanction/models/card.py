from django.db import models

from base.models.abstract_base_model import BaseModel
from organization.models.club import Club
from organization.models.match import Match
from referee.models.referee import Referee


class AbstractCardModel(BaseModel):
    
    match = models.ForeignKey(Match, on_delete=models.CASCADE)

    referee = models.ForeignKey(
        Referee, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True
    )

    match_date = models.DateField()

    # Round but can't use since Python keyword
    stage = models.CharField(max_length=10, null=True, blank=True)

    player_name = models.CharField(max_length=80)

    code = models.CharField(max_length=5, null=True, blank=True)

    minute = models.IntegerField()

    card_desc = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        abstract = True
    

class YellowCard(AbstractCardModel):

    club = models.ForeignKey(
        Club, 
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='yellow_cards'
    )

    # TODO: Clearer related name
    opponent_club = models.ForeignKey(
        Club, 
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='opponent_yellow_cards'
    )

    is_2ct = models.BooleanField(default=False)

    def __str__(self):
        return (
            f'Yellow card for {self.player_name} issued by '
            f'{self.referee.name_common} on {self.match_date}'
        )


class RedCard(AbstractCardModel):
    
    club = models.ForeignKey(
        Club, 
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='red_cards'
    )

    # TODO: Clearer related name
    opponent_club = models.ForeignKey(
        Club, 
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='opponent_red_cards'
    )

    def __str__(self):
        return (
            f'Red card for {self.player_name} issued by '
            f'{self.referee.name_common} on {self.match_date}'
        )
