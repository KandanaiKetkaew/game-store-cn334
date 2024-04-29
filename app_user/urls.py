from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("createacc", view=views.createacc, name="createacc")
    
]
