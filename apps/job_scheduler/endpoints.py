from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponse

from apps.job_scheduler.models import Job


@login_required(login_url="/login/")
def post_synchronize_job(request):
    if request.method == "POST":
        job = Job(type=settings.SYNCHRONIZE, running=False, finished=False, user=request.user)
        job.save()

        return JsonResponse(job_to_dto(job))
    else:
        return HttpResponseNotAllowed(['POST'])


@login_required(login_url="/login/")
def jobs(request):
    if request.method == "POST":
        job = Job(type=request.POST['type'], running=False, finished=False, user=request.user)
        job.save()

        return JsonResponse(job_to_dto(job))
    elif request.method == "GET":
        user_jobs = Job.objects \
            .filter(finished=False) \
            .filter(user_id=request.user.id)

        dtos = []
        for user_job in user_jobs:
            dtos.append(job_to_dto(user_job))

        return JsonResponse(dtos, safe=False)
    else:
        return HttpResponseNotAllowed(['POST', 'GET'])


@login_required(login_url="/login/")
def get_job(request, job_id):
    if request.method == 'GET':
        job = Job.objects.get(id=job_id)

        if request.user.id == job.user_id:
            return JsonResponse(job_to_dto(job))
        else:
            return HttpResponse('Unauthorized', status=401)
    else:
        return HttpResponseNotAllowed(['GET'])


def job_to_dto(job):
    return {
        "id": job.id,
        "type": job.type,
        "running": job.running,
        "finished": job.finished,
        "userId": job.user_id,
    }
