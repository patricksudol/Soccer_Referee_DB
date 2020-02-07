from django.db import models

from base.models.abstract_base_model import BaseModel

class Club(BaseModel):
    
    club_id = models.CharField(max_length=4)

    name = models.CharField(max_length=255, null=True, blank=True)

    is_active = models.BooleanField(default=True)