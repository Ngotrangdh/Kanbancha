from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_img = models.ImageField(upload_to="profile_img")

    def __str__(self):
        return f"{ self.user.username } Profile"

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     with Image.open(self.profile_img.path) as im:
    #         im = im.resize((96, 96))
    #         im.save(self.profile_img.path)
