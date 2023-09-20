from django.contrib import admin
from .models import *

# Register your models here.

class detLocation(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    search_fields = ('name',)
    list_per_page = 10

admin.site.register(Location, detLocation)

class detCharacter(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    search_fields = ('name',)
    list_per_page = 10

admin.site.register(Character, detCharacter)

class detEpisode(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    search_fields = ('name',)
    list_per_page = 10

admin.site.register(Episode, detEpisode)