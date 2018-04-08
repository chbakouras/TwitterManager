from __future__ import absolute_import, print_function

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect

from apps.manager.models import Friend


@login_required(login_url="/login/")
def home(request):
    return redirect('my_friends')


@login_required(login_url="/login/")
def my_friends(request):
    friends = Friend.objects.all()
    return render(request, "friends/index.html", {'friends': friends})


def tweet(request):
    friends = Friend.objects.all()
    return render(request, "friends/index.html", {'friends': friends})


@login_required(login_url="/login/")
def live_search_my_friends(request):
    if request.method == "POST":
        search = request.POST['search']
        friends = Friend.objects.filter(screen_name__icontains=search)

        friendship = request.POST['friendship']
        if friendship != 'all':
            friends = friends.filter(following_back=friendship)

        view = request.POST['view']

        return render(request, "friends/" + view + ".html", {'friends': friends})
    else:
        return HttpResponseNotAllowed(['POST'])
