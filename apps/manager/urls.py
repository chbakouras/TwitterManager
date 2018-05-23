from django.conf.urls import url
from apps.manager import endpoints
from apps.manager import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^my-friends/', views.my_friends, name='my_friends'),
    url(r'^my-tweets/', views.my_tweets, name='my_tweets'),
    url(r'^twitter-search/', views.twitter_search, name='twitter_search'),
    url(r'^twitter-search-live-load/', views.twitter_search_live_load, name='twitter_search_live_load'),
    url(r'^tweets/create/', views.create_tweet, name='create_tweet'),
    url(r'^live-search/', views.live_search_my_friends, name='my_friends_live_search'),

    url(r'^tweets/delete/(?P<tweet_id>[-\w]+)/', endpoints.delete_tweet),
    url(r'^retweet/(?P<tweet_id>[-\w]+)/', endpoints.retweet),
    url(r'^un-follow/(?P<friend_id>[-\w]+)/', endpoints.un_follow),
    url(r'^follow/(?P<friend_id>[-\w]+)/', endpoints.follow),
]
