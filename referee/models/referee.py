from django.db import models

from base.models.BaseModel import BaseModel


class Referee(BaseModel):

    referee_id = models.CharField()

    name_common = models.CharField()

    name_given = models.CharField()

    name_family = models.CharField()

    suffix = models.CharField()

    name_sort = models.CharField()

    name_alt = models.CharField()

    is_active = models.BooleanField()

    is_active_onfield = models.BooleanField()
