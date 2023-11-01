from django.urls import path
from team.views import TeamView

app_name = 'team'

urlpatterns = [
    path('', TeamView.as_view(), name='team'),
]