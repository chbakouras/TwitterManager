from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


@login_required(login_url="login/")
def un_follow(request):
    return JsonResponse()
