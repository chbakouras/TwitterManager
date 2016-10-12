from django.conf import settings
import tweepy


def get_api(request):
    access_tokens = request.user.social_auth.filter(provider='twitter')[0].extra_data['access_token']

    auth = tweepy.OAuthHandler(settings.SOCIAL_AUTH_TWITTER_KEY, settings.SOCIAL_AUTH_TWITTER_SECRET)
    auth.secure = True
    auth.set_access_token(access_tokens['oauth_token'], access_tokens['oauth_token_secret'])
    api = tweepy.API(auth)

    return api
