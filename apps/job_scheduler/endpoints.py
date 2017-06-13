from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseNotAllowed

from apps.job_scheduler.models import Job


@login_required(login_url="/login/")
def post_synchronize_job(request):
    if request.method == "POST":
        job = Job(type=settings.SYNCHRONIZE, running=False, finished=False, user=request.user)
        job.save()

        return JsonResponse({
            "id": job.id,
            "type": job.type,
            "running": job.running,
            "finished": job.finished,
            "userId": job.user_id,
        })
    else:
        return HttpResponseNotAllowed(['POST'])


@login_required(login_url="/login/")
def post_job(request):
    if request.method == "POST":
        job = Job(type=request.POST['type'], running=False, finished=False, user=request.user)
        job.save()

        return JsonResponse({
            "id": job.id,
            "type": job.type,
            "running": job.running,
            "finished": job.finished,
            "userId": job.user_id,
        })
    else:
        return HttpResponseNotAllowed(['POST'])


@login_required(login_url="/login/")
def get_job(request, job_id):
    if request.method == 'GET':
        job = Job.objects.get(id=job_id)

        return JsonResponse({
            "id": job.id,
            "type": job.type,
            "running": job.running,
            "finished": job.finished,
            "userId": job.user_id,
        })
    else:
        return HttpResponseNotAllowed(['GET'])
