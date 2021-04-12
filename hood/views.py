from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Hood, Profile, Business, Post
from django.http import Http404
from .forms import *
from django.contrib.auth import logout as django_logout
from django.contrib.auth.models import User

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
    if request.method == "POST":
        form = HoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit = False)
            hood.save()
        return redirect("home")
    else:
        form = HoodForm()
    return render(request, "main/create_hood.html", {"form": form})

@login_required(login_url='accounts/login/')
def profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("profile")

    else:
        form = ProfileForm()
    return render(request, "main/profile.html", {"form": form, "profile": profile})

@login_required(login_url='accounts/login/')
def post(request):
    posts = Post.objects.all().order_by('-posted_on')
    return render(request, "main/post.html", {"posts": posts})

@login_required(login_url='accounts/login/')
def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit = False)
            post.hood = request.user.profile.neighborhood
            post.posted_by = request.user
            post.save()
            return redirect("post")
    else:
        form = PostForm()
    return render(request, "main/new_post.html", {"form": form})

@login_required(login_url='accounts/login/')
def new_biz(request):
    user = User.objects.filter(id = request.user.id).first()
    profile = Profile.objects.filter(user = user).first()
    if request.method == "POST":
        business_form = BusinessForm(request.POST, request.FILES)
        if business_form.is_valid():
            business = Business(name = request.POST['name'], neighborhood = profile.neighborhood)
            business.save()
        return redirect('business')
    else:
        business_form = BusinessForm()
    return render(request, "main/new_biz.html", {"business": business_form})


@login_required
def logout(request):
    django_logout(request)
    return  HttpResponseRedirect('/')
