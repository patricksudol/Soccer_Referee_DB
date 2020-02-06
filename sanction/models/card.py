from django.db import models

from base.models.abstract_base_model import BaseModel
from organization.models.club import Club
from organization.models.match import Match
from referee.models.referee import Referee


class AbstractCardModel(BaseModel):
    
    match = models.ForeignKey(Match, on_delete=models.CASCADE)

    referee = models.ForeignKey(Referee, on_delete=models.CASCADE)

    match_date = models.DateField()

    _round = models.CharField(max_length=10)

    player_name = models.CharField(max_length=80)

    code = models.CharField(max_length=5)

    minute = models.IntegerField()

    card_desc = models.CharField(max_length=255)

    class __meta__:
        abstract = True


class YellowCard(AbstractCardModel):

    club = models.ForeignKey(
        Club, 
        on_delete=models.CASCADE,
        related_name='yellow_cards'
    )

    # TODO: Clearer related name
    opponent_club = models.ForeignKey(
        Club, 
        on_delete=models.CASCADE,
        related_name='opponent_yellow_cards'
    )

    is_2ct = models.BooleanField(default=False)


class RedCard(AbstractCardModel):
    
    club = models.ForeignKey(
        Club, 
        on_delete=models.CASCADE,
        related_name='red_cards'
    )

    # TODO: Clearer related name
    opponent_club = models.ForeignKey(
        Club, 
        on_delete=models.CASCADE,
        related_name='opponent_red_cards'
    )
