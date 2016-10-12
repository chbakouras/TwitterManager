from __future__ import absolute_import, print_function
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from manager.utils import get_api
import tweepy


@login_required(login_url="login/")
def following(request):
    api = get_api(request)

    friends = []
    for friend in tweepy.Cursor(api.friends).items():
        friends.append(friend)

    return render(request, "page/following.html", {'friends': friends})
