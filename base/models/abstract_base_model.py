import json
import uuid

from collections import OrderedDict
from copy import deepcopy

from django.contrib.auth.models import User
from django.core.serializers import serialize
from django.utils import timezone
from django.db import models, transaction


class BaseModel(models.Model):

    id = models.UUIDField(
        primary_key=True,
        unique=True,
        editable=False,
        default=uuid.uuid4
    )

    created_at = models.DateTimeField(default=timezone.now)

    modified_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(
        User, 
        null=True, 
        related_name='created_%(class)ss', 
        on_delete=models.CASCADE
    )

    modified_by = models.ForeignKey(
        User, 
        null=True, 
        related_name='modified_%(class)ss',
        on_delete=models.CASCADE
    )

    notes = models.TextField(blank=True, default='')

    class Meta:
        abstract = True

    class CleanerMeta:
        fields = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_new = True
        self.original_data = {}

    def _to_dict(self):
        data_json = serialize('json', [self])
        data_dict = json.loads(data_json)[0]['fields']
        return OrderedDict(
            sorted(data_dict.items(), key=lambda x: x[0].lower())
        )

    @classmethod
    def from_db(cls, *args, **kwargs):
        instance = super().from_db(*args, **kwargs)
        instance.is_new = False
        instance.original_data = instance._to_dict()
        return instance

    def create_id(self):
        if not self.id:
            self.id = uuid.uuid4()
    
    def pre_save(self):
        self.create_id()

    @transaction.atomic
    def save(self, *args, **kwargs):
        self.pre_save()
        ret = super().save(*args, **kwargs)
        self.is_new = False
        return ret
    
    def update(self, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)
        self.save()

    def delete(self, *args, **kwargs):
        return super(BaseModel, self).delete(*args, **kwargs)

    def clone(self, commit=False, overrides=None):
        clone = deepcopy(self)
        clone.create_by = None
        clone.created_at = timezone.now()
        clone.pk = None
        clone.is_new = True
        
        overrides = overrides or {}

        for key, value in overrides.items():
            setattr(clone, key, value)

        if commit:
            clone.save()

        return clone
    
    def related_objs_ids_cascade_deleted(self):
        from django.db import router
        from django.db.models.deletion import Collector

        using = router.db_for_write(self.__class__, instance=self)
        collector = Collector(using=using)
        collector.collect([self], keep_parents=False)

        deleted_obj_ids = [obj for v in collector.data.values() for obj in v]
        return deleted_obj_ids

    def add_note(self, notes):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.notes += f'\n{now}: {notes}'
