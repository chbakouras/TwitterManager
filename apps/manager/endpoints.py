from __future__ import absolute_import, print_function

import ast

import logging
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from tweepy import TweepError

from apps.manager.models import Friend
from apps.manager.utils import get_api


logger = logging.getLogger(__name__)


@login_required(login_url="/login/")
def un_follow(request, friend_id):
    api = get_api(request.user)
    try:
        response = api.destroy_friendship(friend_id)

        logger.info(response)
        Friend.objects\
            .filter(twitter_id=friend_id)\
            .delete()

        return JsonResponse(response._json)
    except TweepError as e:
        reason = ast.literal_eval(e.reason)
        return JsonResponse(reason, safe=False)


@login_required(login_url="/login/")
def follow(request, friend_id):
    api = get_api(request.user)
    me = api.me()

    try:
        twitter_friend_json = api.create_friendship(friend_id)._json

        friend = Friend(
            twitter_id=twitter_friend_json['id'],
            profile_image_url=twitter_friend_json['profile_image_url'],
            screen_name=twitter_friend_json['screen_name'],
            user=request.user
        )

        friendships = api.show_friendship(source_id=twitter_friend_json['id'], target_id=me.id)
        for friendship in friendships:
            if friendship.id == twitter_friend_json['id']:
                friend.following_back = friendship.following

        existing_friend = Friend.objects.filter(twitter_id=friend.twitter_id)

        if existing_friend:
            existing_friend.update(
                twitter_id=friend.twitter_id,
                profile_image_url=friend.profile_image_url,
                screen_name=friend.screen_name,
                following_back=friend.following_back
            )
        else:
            friend.save()

        return JsonResponse({}, safe=False)
    except TweepError as e:
        reason = ast.literal_eval(e.reason)
        return JsonResponse(reason, safe=False)
