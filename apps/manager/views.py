from __future__ import absolute_import, print_function

import logging

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect
from tweepy import TweepError

from apps.manager.models import Friend, Tweet
from apps.manager.utils import get_api

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
def my_tweets(request):
    try:
        user = request.user
        api = get_api(user)
        timeline = api.user_timeline()

        for tweet in timeline:
            found_tweet = Tweet.objects.filter(tweet_id=tweet.id_str)

            if found_tweet:
                _update_tweet(found_tweet, tweet)
            else:
                _create_tweet(tweet, user)

        tweets = Tweet.objects \
            .filter(user_id=request.user.id)\
            .order_by('-created_at', '-tweet_id')

        return render(request, "tweets/index.html", {'tweets': tweets})
    except TweepError as error:
        return render(request, "errors/error.html", {'error': error.args[0][0]['message']})


@login_required(login_url="/login/")
def create_tweet(request):
    if request.method == "POST":
        try:
            user = request.user
            api = get_api(user)

            status_text = request.POST['status']
            status = api.update_status(status_text)
            _create_tweet(status, user)

            return redirect('my_tweets')
        except TweepError as error:
            return render(request, "errors/error.html", {'error': error.args[0][0]['message']})
    else:
        return HttpResponseNotAllowed(['POST'])


def twitter_search(request):
    if request.method == "GET":
        return render(request, "twitter-search/index.html", {})
    elif request.method == "POST":
        try:
            user = request.user
            api = get_api(user)

            search = request.POST['search']
            tweets = api.search(search)

            return render(request, "twitter-search/grid.html", {'tweets': tweets})
        except TweepError as error:
            return render(request, "errors/error.html", {'error': error.args[0][0]['message']})
    else:
        return HttpResponseNotAllowed(['POST', 'GET'])


def _create_tweet(status, user):
    if status.text is None:
        status.text = ''
    if status.retweet_count is None:
        status.retweet_count = 0
    if status.retweeted is None:
        status.retweeted = False
    if status.in_reply_to_screen_name is None:
        status.in_reply_to_screen_name = ''

    tweet = Tweet(
        tweet_id=status.id_str,
        created_at=status.created_at,
        text=status.text,
        retweet_count=status.retweet_count,
        retweeted=status.retweeted,
        in_reply_to_screen_name=status.in_reply_to_screen_name,
        user=user
    )

    return tweet.save()


def _update_tweet(tweet, status):
    if status.text is None:
        status.text = ''
    if status.retweet_count is None:
        status.retweet_count = 0
    if status.retweeted is None:
        status.retweeted = False
    if status.in_reply_to_screen_name is None:
        status.in_reply_to_screen_name = ''

    return tweet.update(
        text=status.text,
        retweet_count=status.retweet_count,
        retweeted=status.retweeted,
        in_reply_to_screen_name=status.in_reply_to_screen_name,
    )
