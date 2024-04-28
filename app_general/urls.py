from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('about/', views.about, name='about'),
    path('register', views.register,name='register'),
    path('register/thankyou', views.register_thankyou,name='register_thankyou')
]