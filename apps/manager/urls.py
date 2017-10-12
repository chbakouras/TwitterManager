from django.conf.urls import url
from apps.manager import endpoints

from apps.manager import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^my-friends/', views.my_friends, name='my_friends'),
    url(r'^live-search/', views.live_search_my_friends, name='my_friends_live_search'),
    url(r'^un-follow/(?P<friend_id>[-\w]+)/', endpoints.un_follow),
    url(r'^follow/(?P<friend_id>[-\w]+)/', endpoints.follow),
]
