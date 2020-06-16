from django.urls import path
from django.shortcuts import redirect, reverse
from .views import save_event, save_event_image


urlpatterns = [
    path('save_event/', save_event, name='save_event'),
    path('save_event_image/', save_event_image, name='save_event_image'),
]
