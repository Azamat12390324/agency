from django.shortcuts import render
from django.views.generic import DetailView, ListView
from portfolio.models import Portfolio

app_name = 'portfolio'

class PortfolioView(ListView):
    model = Portfolio
    template_name = 'main/portfolio.html'
