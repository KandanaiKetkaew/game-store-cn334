from django.contrib import admin
from app_gamelist.models import Game


class GameAdmin(admin.ModelAdmin):
    list_display = ['title','price','initial_release']
    search_fields = ['title']

admin.site.register(Game,GameAdmin)