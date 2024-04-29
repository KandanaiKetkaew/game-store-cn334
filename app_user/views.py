from django.shortcuts import render
from app_user.forms import RegisterForm
from django.http import HttpRequest, HttpResponseRedirect
from django.contrib.auth import login
from django.urls import reverse

def createacc(request: HttpRequest):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse("homepage"))
    else:
        form = RegisterForm()
    
    
    context = {"form": form}
    return render(request, "app_user/createacc.html",context)

