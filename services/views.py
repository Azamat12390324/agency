from django.shortcuts import render
from django.views.generic import ListView
from services.models import Service

class ServiceView(ListView):
    model = Service
    template_name = 'main/service.html'
