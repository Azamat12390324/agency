from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from home.models import Home


class HomeView(ListView):
    model = Home
    template_name = 'main/home.html'



