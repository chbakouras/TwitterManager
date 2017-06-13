from django.conf.urls import url

from apps.job_scheduler import endpoints

urlpatterns = [
    url(r'^synchronize/', endpoints.create_synchronize_job),
]
