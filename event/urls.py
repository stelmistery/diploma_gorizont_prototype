from django.urls import path
from django.shortcuts import redirect, reverse
from .views import save_event, events, event_detail, participate

urlpatterns = [
    path('', events, name='events'),
    path('save_event/', save_event, name='save_event'),
    # path('save_event_image/', save_event_image, name='save_event_image'),
    path('detail/<int:pk>', event_detail, name='event_detail'),
    path('<int:pk>participate/<int:user_id>', participate, name='participate'),
]
