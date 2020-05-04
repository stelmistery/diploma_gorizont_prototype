from django.urls import path
from .views import *

urlpatterns = [
    path('form/check/', room_check, name='room_check'),
    # path('form/proc/', booking_procedure, name='book_form'),
    # path('form/processing/', data_confirmation, name='book_conf'),
]
