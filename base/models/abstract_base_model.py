import uuid

from django.db import models


class BaseModel(models.Model):

    id = models.UUIDField(
        primary_key=True, 
        unique=True, 
        editable=False, 
        default=uuid.uuid4
    )

    created_at = models.DateTimeField(default.timezone.now)

    modified_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(
        User, null=True, related_name='created_%(class)ss'
    )

    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_new = True
        self.original_data = {}
