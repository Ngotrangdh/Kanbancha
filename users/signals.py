from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from .models import Profile


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.create(
            user=instance, profile_img="profile_img/default.png"
        )
        profile.save()
