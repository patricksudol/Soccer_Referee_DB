from django.db import models

from base.models.abstract_base_model import BaseModel
from organization.models.club import Club
from organization.models.match import Match
from referee.models.referee import Referee


class Penalty(BaseModel):

    match = models.ForeignKey(Match, on_delete=models.CASCADE)

    referee = models.ForeignKey(Referee, on_delete=models.CASCADE)

    match_date = models.DateField()

    _round = models.CharField(max_length=10)

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

    minute = models.IntegerField()

    foul_desc = models.CharField(max_length=127)
