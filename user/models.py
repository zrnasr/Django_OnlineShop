from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

phone_validator = RegexValidator(r'^(?:0|98|\+98|\+980|0098|098|00980)?(9\d{9})$')

class User(AbstractUser):
    username = None
    email = None
    phone = models.CharField(("phone_num"), max_length=15, unique=True, validators=[phone_validator])
    USERNAME_FIELD = 'phone'



class Profile(User):
    postal_code = models.BigIntegerField(('postal_code'), max_length=25)
    city = models.CharField(('city'), max_length=30)
    home_address = models.TextField('address')

    