

from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save

def create_auth_token(sender, instance, created, **kwargs):
    if created:
        token = Token.objects.create(user=instance)
        print(token)




