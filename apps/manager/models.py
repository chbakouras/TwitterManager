from django.contrib.auth.models import User
from django.db import models


class Friend(models.Model):
    twitter_id = models.CharField(max_length=30)
    profile_image_url = models.CharField(max_length=200)
    profile_background_image_url = models.CharField(max_length=200, default='')
    screen_name = models.CharField(max_length=50)
    following_back = models.BooleanField(default=False)
    favourites_count = models.BigIntegerField(default=0)
    followers_count = models.BigIntegerField(default=0)
    friends_count = models.BigIntegerField(default=0)
    statuses_count = models.BigIntegerField(default=0)
    description = models.CharField(max_length=400, default='')
    location = models.CharField(max_length=200, default='')
    name = models.CharField(max_length=200, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Tweet(models.Model):
    tweet_id = models.CharField(max_length=200)
    created_at = models.DateField()
    text = models.CharField(max_length=200, default='')
    retweet_count = models.BigIntegerField(default=0)
    retweeted = models.BooleanField(default=True)
    in_reply_to_screen_name = models.CharField(max_length=200, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
