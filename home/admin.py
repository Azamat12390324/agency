from django.contrib import admin
from home.models import Home 

@admin.register(Home)
class Home(admin.ModelAdmin):
    list_display = ('title', 'small_title')
    list_display_links = ('title', 'small_title')



