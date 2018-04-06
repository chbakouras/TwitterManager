import tweepy
from django.conf import settings


def get_api(user):
    access_tokens = user.social_auth.filter(provider='twitter')[0].extra_data['access_token']

    auth = tweepy.OAuthHandler(settings.SOCIAL_AUTH_TWITTER_KEY, settings.SOCIAL_AUTH_TWITTER_SECRET)
    auth.secure = True
    auth.set_access_token(access_tokens['oauth_token'], access_tokens['oauth_token_secret'])
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    return api
