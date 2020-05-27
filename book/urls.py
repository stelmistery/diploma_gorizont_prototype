from django.urls import path
from django.shortcuts import redirect, reverse
from .views import *
# from .forms import ContactForm1, ContactForm2
# from .views import BookWizard

app_name = 'book'

urlpatterns = [
    path('check/', room_check, name='room_check'),
    path('process/', book_process, name='book_form'),
    path('confirmed/', book_confirmed, name='book_conf'),

]
