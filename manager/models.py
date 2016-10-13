from django.contrib.auth.models import User
from django.db import models


class Friend(models.Model):
    twitter_id = models.CharField(max_length=30)
    profile_image_url = models.CharField(max_length=200)
    screen_name = models.CharField(max_length=50)
    following_back = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
