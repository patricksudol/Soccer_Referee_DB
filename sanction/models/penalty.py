from django.db import models

from base.models.BaseModel import BaseModel
from organization.models.club import Club
from organization.models.match import Match
from referee.models.referee import Referee


class Penalty(BaseModel):

    match = models.ForeignKey(Match)

    referee = models.ForeignKey(Referee)

    match_date = models.DateField()

    _round = models.CharField()

    club = models.ForeignKey(Club)

    opponent_club = models.ForeignKey(Club)

    order = models.IntegerField()

    minute = models.IntegerField()

    foul_desc = models.CharField()
