from django.contrib.auth.decorators import login_required
from django.core.management import call_command
from django.http import HttpResponse


@login_required(login_url="/login/")
def create_synchronize_job(request):

    call_command('synchronize', request.user.id, interactive=False)

    return HttpResponse('')