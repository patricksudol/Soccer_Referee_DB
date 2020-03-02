from django.db import models
from django.forms.models import model_to_dict

from base.constants import DAYS_OF_WEEK, RESULTS
from base.models.abstract_base_model import BaseModel
from organization.models.club import Club
from organization.models.season import Season
from referee.models.referee import Referee


class Match(BaseModel):

    match_id = models.CharField(max_length=12)

    season = models.ForeignKey(Season, on_delete=models.CASCADE)

    match_date = models.DateField()

    week = models.IntegerField(null=True, blank=True)

    day = models.CharField(
        choices=DAYS_OF_WEEK, 
        max_length=1, 
        null=True, 
        blank=True
    )

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

    result = models.CharField(choices=RESULTS, max_length=1)

    # Round but it is a Python keywoard so can not use
    stage = models.CharField(max_length=10, null=True, blank=True)

    leg = models.IntegerField(null=True, blank=True)

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
        related_name='fourth_official_matches',
        null=True,
        blank=True
    )

    var = models.ForeignKey(
        Referee, 
        on_delete=models.CASCADE,
        related_name='var_matches',
        null=True,
        blank=True
    )

    avar = models.ForeignKey(
        Referee, 
        on_delete=models.CASCADE,
        related_name='avar_matches',
        null=True,
        blank=True
    )

    fifth_official = models.ForeignKey(
        Referee, 
        on_delete=models.CASCADE,
        related_name='fifth_official_matches',
        null=True,
        blank=True
    )

    total_fouls = models.IntegerField(default=0)

    home_fouls = models.IntegerField(default=0)

    away_fouls = models.IntegerField(default=0)

    total_cards_yellow = models.IntegerField(default=0)

    home_cards_yellow = models.IntegerField(default=0)

    away_cards_yellow = models.IntegerField(default=0)

    total_cards_red = models.IntegerField(default=0)

    home_cards_red = models.IntegerField(default=0)

    away_cards_red = models.IntegerField(default=0)

    total_penalties = models.IntegerField(default=0)

    home_penalties = models.IntegerField(default=0)

    away_penalties = models.IntegerField(default=0)

    @property
    def is_sanction(self):
        return bool(
            self.yellowcard_set.all() or self.redcard_set.all() or self.penalties.all()
        )

    @property
    def full_crew(self):
        crew_dictionary = {
            'referee': self.referee,
            'ar1': self.ar1,
            'ar2': self.ar2,
            'fourth_offical': self.fourth_official,
        }

        if self.var:
            crew_dictionary.update({'var': self.var})
        if self.avar:
            crew_dictionary.update({'avar': self.avar})
        if self.fifth_official:
            crew_dictionary.update({'fifth_official': self.fifth_official})
        return crew_dictionary

    # @property
    # def yellow_cards(self):
    #     return self.yellowcard_set.all()

    # @property
    # def red_cards(self):
    #     return self.redcard_set.all()

    # @property
    # def penalties(self):
    #     return self.penalties.all()

    def __str__(self):
        return (
            f'{self.match_date}: {self.home_club}'
            f'[{self.home_score}] vs {self.away_club}[{self.away_score}]'
        )

    def referee_position(self, referee):
        position_mapping = {
            'referee': 'Referee',
            'ar1': 'AR1',
            'ar2': 'AR2', 
            'fourth_official': 'Fourth Official',
            'var': 'VAR',
            'avar': 'AVAR',
            'fifth_official': 'Fifth Official'
        }

        positions_dict = model_to_dict(self, fields=[
            'referee',
            'ar1',
            'ar2',
            'fourth_official',
            'var',
            'avar',
            'fifth_official'
        ])
        position = [position for position, r_id in positions_dict.items() if referee.id == r_id][0]
        return position_mapping[position] if position else None
