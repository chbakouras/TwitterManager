from django.conf.urls import url
from apps.manager import endpoints

from apps.manager import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^following/', views.following, name='following'),
    url(r'^un-follow/(?P<friend_id>[-\w]+)/', endpoints.un_follow),
    url(r'^follow/(?P<friend_id>[-\w]+)/', endpoints.follow),
    url(r'^synchronize/', endpoints.synchronize),
]
