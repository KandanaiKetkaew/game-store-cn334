from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('about/', views.about, name='about'),
    path('register', views.register,name='register'),
    path('register/thankyou', views.register_thankyou,name='register_thankyou'),
    path('cart', views.cart,name='cart'),
    path('checkout', views.checkout,name='checkout'),
    path('cart/<int:game_id>/', views.cart, name='cart'),
]