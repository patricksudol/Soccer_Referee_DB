from django.db import models

from base.models.abstract_base_model import BaseModel
from organization.models.club import Club
from organization.models.season import Season
from referee.models.referee import Referee


class Match(BaseModel):

    match_id = models.CharField(max_length=12)

    season = models.ForeignKey(Season, on_delete=models.CASCADE)

    match_date = models.DateField()

    week = models.IntegerField()

    day = models.CharField(max_length=1)

    home_club = models.ForeignKey(
        Club, 
        on_delete=models.CASCADE,
        related_name='home_matches'
    )

    away_club = models.ForeignKey(
        Club, 
        on_delete=models.CASCADE,
        related_name='away_matches'
    )

    home_score = models.IntegerField()

    away_score = models.IntegerField()

    result = models.CharField(max_length=1)

    _round = models.CharField(max_length=10)

    leg = models.IntegerField()

    referee = models.ForeignKey(
        Referee, 
        on_delete=models.CASCADE,
        related_name='referee_matches'
    )

    ar1 = models.ForeignKey(
        Referee, 
        on_delete=models.CASCADE,
        related_name='ar1_matches'
    )

    ar2 = models.ForeignKey(
        Referee, 
        on_delete=models.CASCADE,
        related_name='ar2_matches'
    )

    fourth_official = models.ForeignKey(
        Referee, 
        on_delete=models.CASCADE,
        related_name='fourth_official_matches'
    )

    var_id = models.ForeignKey(
        Referee, 
        on_delete=models.CASCADE,
        related_name='var_matches'
    )

    avar_id = models.ForeignKey(
        Referee, 
        on_delete=models.CASCADE,
        related_name='avar_matches'
    )

    fifth_official_id = models.ForeignKey(
        Referee, 
        on_delete=models.CASCADE,
        related_name='fifth_official_matches'
    )

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





    