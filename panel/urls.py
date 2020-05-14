from django.contrib import admin
from django.urls import path
from .views import index, BookListView, CustomerDetailView, book_success, book_detail

urlpatterns = [
    path('', index, name='panel_index'),
    path('books/', BookListView.as_view(), name='book_list'),
    path('bookdetail/', book_detail, name='book_view'),
    path('customer/<int:pk>', CustomerDetailView.as_view(), name='customer_view'),
    path('book/<int:pk>/success', book_success, name='book_success'),
]

