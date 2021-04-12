from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Hood, Profile, Business, Post
from django.http import Http404
from .forms import *

# Create your views here.
@login_required(login_url='accounts/login/')
def index(request):
    try:
        hoods = Hood.objects.all()
    except Exception as e:
        raise Http404
    return render(request, "main/index.html", {"hoods": hoods})

@login_required(login_url='accounts/login/')
def create_hood(request):
    current_user = request.user
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit = False)
            hood.user = current_user
            hood.save()
        return redirect("home")
    else:
        form = HoodForm()
    return render(request, "main/create_hood.html", {"form": form})

@login_required(login_url='accounts/login/')
def profile(request):
    current_user = request.user
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.user = current_user
            profile.save()
        return HttpResponseRedirect('profile')
    else:
        form = ProfileForm()
    
    try:
        profile = Profile.object.filter(user = current_user)
    except Exception as e:
        raise Http404
    return render(request, "main/profile.html", {"form": form, "profile": profile})
