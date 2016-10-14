from django.conf.urls import url, include
from django.contrib.auth import views

urlpatterns = [
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^login/$', views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', views.logout, {'next_page': '/login'}, name='logout'),
]
