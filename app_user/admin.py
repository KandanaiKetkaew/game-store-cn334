from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from app_user.models import CustomUser

admin.site.register(CustomUser,UserAdmin)