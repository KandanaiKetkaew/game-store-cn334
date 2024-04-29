from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

class Profile(models.Model):
    address = models.TextField(default="")
    phone = models.CharField(max_length=15, default="")
    user = models.OneToOneField("app_user.CustomUser", on_delete=models.CASCADE)