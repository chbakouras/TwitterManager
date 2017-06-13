from __future__ import absolute_import, print_function

import ast

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from tweepy import TweepError

from apps.manager.utils import get_api


@login_required(login_url="/login/")
def un_follow(request, friend_id):
    api = get_api(request.user)
    try:
        response = api.destroy_friendship(friend_id)
        return JsonResponse(response._json)
    except TweepError as e:
        reason = ast.literal_eval(e.reason)
        return JsonResponse(reason, safe=False)


@login_required(login_url="/login/")
def follow(request, friend_id):
    api = get_api(request.user)
    try:
        response = api.create_friendship(friend_id)
        return JsonResponse(response._json)
    except TweepError as e:
        reason = ast.literal_eval(e.reason)
        return JsonResponse(reason, safe=False)
