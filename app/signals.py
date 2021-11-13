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


@receiver(post_save, sender=Profile)
def UpdateUser(sender, instance, created, **kwargs):
    data = instance
    user = data.user
    if created == False:
        user.first_name = data.name
        user.save()


@receiver(post_delete, sender=Profile)
def DeleteUser(sender, instance, **kwargs):
    try:
        user = instance.user
        user.delete()
    except:
        pass
