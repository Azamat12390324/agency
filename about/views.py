from django.shortcuts import render
from about.models import About
from django.views.generic import ListView

class AboutView(ListView):
    model = About
    template_name = 'main/about.html'
