from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # link each user to one and only one profile
    discord_username = models.CharField(max_length=30, blank=True, null=True)
    discord_id = models.CharField(max_length=30, blank=True, null=True)
    discord_webhook = models.URLField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.username
