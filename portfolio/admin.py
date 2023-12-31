from django.contrib import admin

from portfolio.models import Portfolio


@admin.register(Portfolio)
class Portfolio(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title', )