from django.apps import AppConfig
from django.apps import AppConfig
from django.db.models.signals import post_save


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'

    def ready(self):
        from user.signal import create_auth_token
        from user.models import User
        post_save.connect(create_auth_token, sender=User)