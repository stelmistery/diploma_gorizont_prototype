from django.contrib import admin
from django.urls import path
from .views import index, BookListView, customer_detail_view, book_success, book_view, book_view_detail

urlpatterns = [
    path('', index, name='panel_index'),
    path('books/', BookListView.as_view(), name='book_list'),
    path('book/detail/', book_view, name='book_view'),
    # path('book/edit/', book_edit, name='book_edit'),
    path('book/detail/<int:pk>', book_view_detail, name='book_view_detail'),
    path('customer/<int:pk>', customer_detail_view, name='customer_view'),
    path('book/<int:pk>/success', book_success, name='book_success'),
    # path('book/<int:pk>/success', book_success, name='customer_view'),
]

