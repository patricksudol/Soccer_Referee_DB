from django.db import models

from base.models.abstract_base_model import BaseModel


class Referee(BaseModel):

    referee_id = models.CharField(max_length=7)

    name_common = models.CharField(max_length=80)

    name_given = models.CharField(max_length=40)

    name_family = models.CharField(max_length=40)

    suffix = models.CharField(max_length=10, null=True, blank=True)

    name_sort = models.CharField(max_length=80)

    name_alt = models.CharField(max_length=80)

    is_active = models.BooleanField(default=False)

    is_active_onfield = models.BooleanField(default=False)

    image_path = models.CharField(max_length=255, null=True, blank=True)

    @property
    def is_referee(self):
        return bool(self.referee_matches.count())

    @property
    def ar_assignments(self):
        return self.ar1_matches.all() | self.ar2_matches.all()

    @property
    def all_assignments(self):
        return (
            self.referee_matches.all() | self.ar1_matches.all() | 
            self.ar2_matches.all() | self.fourth_official_matches.all() |
            self.var_matches.all() | self.avar_matches.all() | 
            self.fifth_official_matches.all()
        )

    @property
    def yellow_card_count(self):
        return self.yellowcard_set.count()

    @property
    def red_card_count(self):
        return self.redcard_set.count()

    @property
    def first_match(self):
        return self.all_assignments.order_by('match_date').first()

    @property
    def last_match(self):
        return self.all_assignments.order_by('match_date').last()

    # Hacky AF but placeholder into I can collect all images and host locally
    @property
    def image_url(self):
        url = (
            f'http://proreferees.com/wp-content/uploads/2020/02/2020-'
            f'{self.name_given}-{self.name_family}.jpg'
        )
        return self.image_path if self.image_path else url

    def __str__(self):
        status = 'active' if self.is_active else 'not active'
        return f'{self.name_common} [{self.referee_id}] is {status}'
