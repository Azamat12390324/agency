from django.contrib import admin
from about.models import About

@admin.register(About)
class About(admin.ModelAdmin):
    list_display = ('title', 'sub_title')
    list_display_links = ('title',  'sub_title')