from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='accounts/login/')
def index(request):
    if request.method == "POST":
        form = P
    return render(request, "main/index.html")