from django.db import models

from base.models.BaseModel import BaseModel


class Season(BaseModel):

    season = models.CharField()

    date_begin = models.DateField()

    date_end_reg = models.DateField()

    date_begin_playoffs = models.DateField()

    date_end_playoffs = models.DateField()