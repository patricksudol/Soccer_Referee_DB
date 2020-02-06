from django.db import models

from base.models.BaseModel import BaseModel
from organization.models.club import Club
from organization.models.match import Match
from referee.models.referee import Referee


class AbstractCardModel(BaseModel):
    
    match = models.ForeignKey(Match)

    referee = models.ForeignKey(Referee)

    match_date = models.DateField()

    _round = models.CharField()

    club = models.ForeignKey(Club)

    opponent_club = models.ForeignKey(Club)

    player_name = models.CharField()

    code = models.CharField()

    minute = models.IntegerField()

    card_desc = models.CharField()

    class __meta__:
        abstract = True


class YellowCard(AbstractCardModel):

    is_2ct = models.BooleanField(default=False)


class RedCard(AbstractCardModel):
    pass
