from django.db.models.signals import *
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import *
from django.conf import settings


@receiver(post_save, sender=User)
def CreatedProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            name=user.first_name
        )
