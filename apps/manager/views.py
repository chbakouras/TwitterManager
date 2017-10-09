from __future__ import absolute_import, print_function

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from apps.manager.models import Friend


@login_required(login_url="/login/")
def home(request):
    return redirect('my_friends')


@login_required(login_url="/login/")
def my_friends(request):
    friends = Friend.objects.all()
    return render(request, "page/friends.html", {'friends': friends})
