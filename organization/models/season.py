from django.db import models

from base.models.abstract_base_model import BaseModel


class Season(BaseModel):

    season = models.IntegerField()

    date_begin = models.DateField(null=True, blank=True)

    date_end_reg = models.DateField(null=True, blank=True)

    date_begin_playoffs = models.DateField(null=True, blank=True)

    date_end_playoffs = models.DateField(null=True, blank=True)
