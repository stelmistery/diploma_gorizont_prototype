from django.urls import path
from django.shortcuts import redirect, reverse
from .views import save_event


urlpatterns = [
    path('save_event/', save_event, name='save_event'),
]
