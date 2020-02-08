from django.db import models

from base.models.abstract_base_model import BaseModel
from organization.models.club import Club
from organization.models.match import Match
from referee.models.referee import Referee


class Penalty(BaseModel):

    match = models.ForeignKey(
        Match, 
        on_delete=models.CASCADE, 
        related_name='penalties'
    )

    referee = models.ForeignKey(
        Referee, 
        on_delete=models.CASCADE,
        null=True,
        blank=True, 
        related_name='penalties'
    )

    match_date = models.DateField()

    # Round but can't use since Python keyword
    stage = models.CharField(max_length=10, null=True, blank=True)

    club = models.ForeignKey(
        Club, 
        on_delete=models.CASCADE,
        related_name='penalties'
    )

    # TODO: Clearer related name
    opponent_club = models.ForeignKey(
        Club, 
        on_delete=models.CASCADE,
        related_name='opponent_penalties'
    )

    order = models.IntegerField()

    minute = models.IntegerField(null=True, blank=True)

    foul_desc = models.CharField(max_length=127, null=True, blank=True)

    def __str__(self):
        return (
            f'Penalty awarded against {self.club} issued by '
            f'{self.referee.name_common}'
        )