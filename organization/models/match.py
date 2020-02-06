from django.db import models

from base.models.BaseModel import BaseModel
from organization.models.club import Club
from organization.models.season import Season
from referee.models.referee import Referee


class Match(BaseModel):

    match_id = models.CharField()

    season = models.ForeignKey(Season)

    match_date = models.DateField()

    week = models.IntegerField()

    day = models.CharField()

    home_club = models.ForeignKey(Club)

    away_club = models.ForeignKey(Club)

    home_score = models.IntegerField()

    away_score = models.IntegerField()

    result = models.CharField()

    _round = models.CharField()

    leg = models.IntegerField()

    referee = models.ForeignKey(Referee)

    ar1 = models.ForeignKey(Referee)

    ar2 = models.ForeignKey(Referee)

    fourth_official = models.ForeignKey(Referee)

    var_id = models.ForeignKey(Referee)

    avar_id = models.ForeignKey(Referee)

    fifth_official_id = models.ForeignKey(Referee)

    total_fouls = models.IntegerField()

    home_fouls = models.IntegerField()

    away_fouls = models.IntegerField()

    total_cards_yellow = models.IntegerField()

    home_cards_yellow = models.IntegerField()

    away_cards_yellow = models.IntegerField()

    total_cards_red = models.IntegerField()

    home_cards_red = models.IntegerField()

    away_card_red = models.IntegerField()

    total_penalties = models.IntegerField()

    home_penalties = models.IntegerField()

    away_penalties = models.IntegerField()





    