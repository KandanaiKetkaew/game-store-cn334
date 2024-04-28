from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from app_general.forms import RegisterModelForm
from .models import Register

def home(request):
    return render(request,'app_general/home.html')

def about(request):
    return render(request,'app_general/about.html')

def register(request):
    if request.method =='POST':
        form = RegisterModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('register_thankyou'))
    else:
        form = RegisterModelForm()
    context = {'form': form}
    return render(request,'app_general/register.html', context)

def register_thankyou(request):
    return render(request,'app_general/register_thankyou.html')