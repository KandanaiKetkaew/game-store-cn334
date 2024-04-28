from django import forms
from app_gamelist.models import Game
from .models import Register


class RegisterModelForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['name','email']
        