from django.contrib import admin
from app_general.models import Register

class RegisterAdmin(admin.ModelAdmin):
    list_display = ['name','email','status','registered_at']
    search_fields = ['name','email']
    list_filter = ['status']

admin.site.register(Register, RegisterAdmin)
