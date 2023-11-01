from django.urls import path
from services.views import ServiceView

app_name = 'service'

urlpatterns = [
    path('', ServiceView.as_view(), name='service'),

]