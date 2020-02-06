from django.db import models

from base.models.BaseModel import BaseModel

class Club(BaseModel):
    
    club_id = models.CharField()

    name = models.CharField()

    is_active = models.BooleanField(default=True)