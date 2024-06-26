from django import forms
from django.contrib.auth.forms import UserCreationForm
from app_user.models import CustomUser, Profile




class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("email",)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["first_name","last_name"]
        
        
class ExtendedProfileForm(forms.ModelForm):
    prefix = "extended"
    class Meta:
        model = Profile 
        fields = ["address", "phone"]
        widgets = {
            "address": forms.Textarea(attrs={"rows": 2})
        }

