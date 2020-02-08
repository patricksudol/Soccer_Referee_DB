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

    def __str__(self):
        status = 'active' if self.is_active else 'not active'
        return f'{self.name_common} [{self.referee_id}] is {status}'
