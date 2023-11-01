from django.shortcuts import render
from contact.models import Contact
from django.views.generic import ListView




class ContactView(ListView):
    model = Contact
    template_name = 'main/contact.html'

