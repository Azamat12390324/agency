from django.contrib import admin
from django.contrib import admin
from contact.models import Contact

@admin.register(Contact)
class Contact(admin.ModelAdmin):
    list_display = ('title', 'name', 'email', 'phone')
    list_display_links = ('name',)
    list_filter = ('name',)
    list_editable = ('email', 'phone')


