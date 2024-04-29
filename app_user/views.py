from django.shortcuts import render
from app_user.forms import RegisterForm
from django.http import HttpRequest, HttpResponseRedirect
from django.contrib.auth import login
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm , UserProfileForm , ExtendedProfileForm 

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

@login_required
def dashboard(request: HttpRequest):
    return render(request, "app_user/dashboard.html",)

@login_required
def profile(request: HttpRequest):
    user = request.user
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        is_new_profile = False
        try:
            extended_form = ExtendedProfileForm(request.POST,instance=user.profile)
        except:
            extended_form = ExtendedProfileForm(request.POST)
            is_new_profile = True
            
            
            
        if form.is_valid() and extended_form.is_valid():
            form.save()
            if is_new_profile:
                profile = extended_form.save(commit=False)
                profile.user = user
                profile.save()
            else:
                extended_form.save()
                
            return HttpResponseRedirect(reverse("profile"))
    
    else:
        form = UserProfileForm(instance=user)
        try:
            extended_form = ExtendedProfileForm(instance=user.profile)
        except:
            extended_form = ExtendedProfileForm()
    
    context = {
        "form": form,
        "extended_form": extended_form
    }
    return render (request, "app_user/profile.html", context)