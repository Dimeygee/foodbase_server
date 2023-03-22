from .models import (User, MyProfile)
from django.db.models.signals import post_save
from django.dispatch import receiver
import random


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        MyProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.myprofile.save()