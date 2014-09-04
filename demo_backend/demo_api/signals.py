from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token


@receiver(post_save, sender=User)
def init_new_user(sender, instance, signal, created, **kwargs):
    """
    Create an authentication token for newly created users.
    """
    if created:
        Token.objects.get_or_create(user=instance)
