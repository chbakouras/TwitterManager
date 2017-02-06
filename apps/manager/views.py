from __future__ import absolute_import, print_function

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from apps.manager.models import Friend


@login_required(login_url="/login/")
def home(request):
    return redirect('following')


@login_required(login_url="/login/")
def following(request):
    friends = Friend.objects.all()
    return render(request, "page/following.html", {'friends': friends})
