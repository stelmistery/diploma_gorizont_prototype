from django.urls import path
from django.shortcuts import redirect, reverse
from .views import *
# from .forms import ContactForm1, ContactForm2
# from .views import BookWizard

initial = {}

urlpatterns = [
    path('form/check/', room_check, name='room_check'),
    path('form/process/', book_process, name='book_form'),
    path('form/confirmed/', book_confirmed, name='book_conf'),
    # path('test/', index, name='test'),
    # path('form/processing/', data_confirmation, name='book_conf'),
    # path('contact/', BookWizard.as_view(FORMS, initial_dict=initial)),
]
