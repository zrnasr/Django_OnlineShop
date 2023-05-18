from django.db import models
from django.contrib.auth.models import AbstractUser

class BaseModel(models.Model):
    class Meta():
        abstract = True

    is_deleted = models.BooleanField(default=False, null=False, blank=False)


class User(AbstractUser):
    pass