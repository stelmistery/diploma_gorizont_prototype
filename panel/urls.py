from django.contrib import admin
from django.urls import path
from .views import index, BookDetailView, BookListView, CustomerDetailView

urlpatterns = [
    path('', index, name='panel_index'),
    path('books/', BookListView.as_view(), name='orders'),
    path('bookdetail/<int:pk>', BookDetailView.as_view(), name='book_view'),
    path('customer/<int:pk>', CustomerDetailView.as_view(), name='customer_view'),
]

