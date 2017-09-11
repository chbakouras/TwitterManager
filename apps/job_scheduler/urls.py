from django.conf.urls import url

from apps.job_scheduler import endpoints

urlpatterns = [
    url(r'^synchronize/$', endpoints.post_synchronize_job),

    url(r'^jobs/$', endpoints.jobs),
    url(r'^jobs/(?P<job_id>[0-9]+)/$', endpoints.get_job),
]
