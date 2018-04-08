from __future__ import absolute_import, print_function

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect
from tweepy import TweepError

from apps.manager.models import Friend, Tweet
from apps.manager.utils import get_api
import logging

logger = logging.getLogger(__name__)


@login_required(login_url="/login/")
def home(request):
    return redirect('my_friends')


@login_required(login_url="/login/")
def my_friends(request):
    friends = Friend.objects \
        .filter(user_id=request.user.id)

    return render(request, "friends/index.html", {'friends': friends})


@login_required(login_url="/login/")
def live_search_my_friends(request):
    if request.method == "POST":
        search = request.POST['search']
        friends = Friend.objects \
            .filter(screen_name__icontains=search) \
            .filter(user_id=request.user.id)

        friendship = request.POST['friendship']
        if friendship != 'all':
            friends = friends.filter(following_back=friendship)

        view = request.POST['view']

        return render(request, "friends/" + view + ".html", {'friends': friends})
    else:
        return HttpResponseNotAllowed(['POST'])


@login_required(login_url="/login/")
def get_tweets(request):
    tweets = Tweet.objects \
        .filter(user_id=request.user.id)

    return render(request, "tweets/index.html", {'tweets': tweets})


@login_required(login_url="/login/")
def create_tweet(request):
    if request.method == "POST":
        try:
            user = request.user
            api = get_api(user)

            status_text = request.POST['status']
            status = api.update_status(status_text)

            tweet = Tweet(
                tweet_id=status.id_str,
                created_at=status.created_at,
                text=status.text,
                retweet_count=status.retweet_count,
                retweeted=status.retweeted,
                in_reply_to_screen_name=status.in_reply_to_screen_name,
                user=user
            )
            tweet.save()

            return redirect('get_tweets')
        except TweepError as error:
            return render(request, "errors/error.html", {'error': error})
    else:
        return HttpResponseNotAllowed(['POST'])
