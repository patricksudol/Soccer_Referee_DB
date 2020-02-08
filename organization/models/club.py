from django.db import models

from base.models.abstract_base_model import BaseModel


class Club(BaseModel):
    
    club_id = models.CharField(max_length=4)

    name = models.CharField(max_length=255, null=True, blank=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        status = 'active' if self.is_active else 'not active'
        return f'{self.name} [{self.club_id}] is {status}'
