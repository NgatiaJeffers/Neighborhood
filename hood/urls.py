from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path("add_hood/", views.create_hood, name = "add_hood"),
    path("profile/", views.profile, name = "profile"),
]