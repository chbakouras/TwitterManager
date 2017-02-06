from __future__ import absolute_import, print_function

import ast

import tweepy
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import JsonResponse
from manager.models import Friend
from tweepy import TweepError

from apps.manager.utils import get_api


@login_required(login_url="/login/")
def un_follow(request, friend_id):
    api = get_api(request)
    try:
        response = api.destroy_friendship(friend_id)
        return JsonResponse(response._json)
    except TweepError as e:
        reason = ast.literal_eval(e.reason)
        return JsonResponse(reason, safe=False)


@login_required(login_url="/login/")
def follow(request, friend_id):
    api = get_api(request)
    try:
        response = api.create_friendship(friend_id)
        return JsonResponse(response._json)
    except TweepError as e:
        reason = ast.literal_eval(e.reason)
        return JsonResponse(reason, safe=False)


@login_required(login_url="/login/")
def synchronize(request):
    api = get_api(request)

    me = api.me()
    for twitterFriend in tweepy.Cursor(api.friends).items():
        friend = Friend(
            twitter_id=twitterFriend.id,
            profile_image_url=twitterFriend.profile_image_url,
            screen_name=twitterFriend.screen_name,
            user=request.user
        )

        friendships = api.show_friendship(source_id=twitterFriend.id, target_id=me.id)
        for friendship in friendships:
            if friendship.id == twitterFriend.id:
                friend.following_back = friendship.following

        existing = Friend.objects.filter(twitter_id=friend.twitter_id)

        if existing:
            existing.update(
                twitter_id=friend.twitter_id,
                profile_image_url=friend.profile_image_url,
                screen_name=friend.screen_name,
                following_back=friend.following_back
            )
        else:
            friend.save()

    return HttpResponse('')
