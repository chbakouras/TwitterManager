from django.conf.urls import url
from manager import views
from manager import endpoints

urlpatterns = [
    url(r'^following/', views.following, name='following'),
    url(r'^un-follow/', endpoints.un_follow),
]
