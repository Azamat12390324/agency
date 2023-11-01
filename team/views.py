from django.shortcuts import render
from django.shortcuts import render
from team.models import Team
from django.views.generic import ListView

class TeamView(ListView):
    model = Team
    template_name = 'main/team.html'

