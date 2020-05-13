from django.contrib import admin
from django.urls import path
from .views import index, orders

urlpatterns = [
    path('orders/', orders, name='orders'),
    path('', index, name='panel_index'),
]
