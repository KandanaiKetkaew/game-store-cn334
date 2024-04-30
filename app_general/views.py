from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from app_general.forms import RegisterModelForm
from .models import Register
from app_gamelist.models import Game
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


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

@csrf_exempt
def cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        game_id = data.get('game_id')
        game = get_object_or_404(Game, id=game_id)
        cart_image = game.image_relative_url
        cart_title = game.title
        cart_price = game.price
        response_data = {
            'message': 'Added to cart successfully',
            'game_title': cart_title,
            'game_price': cart_price
        }
        return JsonResponse(response_data)
    else:
        return render(request, 'app_general/cart.html')



def checkout(request):
    return render(request,'app_general/checkout.html')