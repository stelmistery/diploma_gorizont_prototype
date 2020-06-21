from django.urls import path
from .views import save_event, events, event_detail, participate

urlpatterns = [
    path('', events, name='events'),
    path('save_event/', save_event, name='save_event'),
    path('detail/<int:pk>', event_detail, name='event_detail'),
    path('<int:pk>participate/<int:user_id>', participate, name='participate'),
]
