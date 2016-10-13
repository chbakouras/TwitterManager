from __future__ import absolute_import, print_function

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from manager.models import Friend


@login_required(login_url="login/")
def following(request):
    friends = Friend.objects.all()
    return render(request, "page/following.html", {'friends': friends})
