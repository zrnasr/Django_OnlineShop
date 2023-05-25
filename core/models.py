from django.db import models


class BaseModel(models.Model):
    class Meta():
        abstract = True

    is_deleted = models.BooleanField(default=False, null=False, blank=False)
