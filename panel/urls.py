from django.contrib import admin
from django.urls import path
from .views import index, BookListView, book_view, book_view_detail, book_success, customer_view, customer_detail_view, \
    book_create, book_check, event_list, panel_event_view_detail, event_success, panel_event_post, orderer_detail_view, \
    orderer_view

urlpatterns = [
    path('', index, name='panel_index'),
    path('books/', BookListView.as_view(), name='book_list'),
    path('book/detail/', book_view, name='book_view'),
    path('book/create/', book_create, name='book_create'),
    path('book/check/', book_check, name='book_check'),
    path('book/detail/<int:pk>', book_view_detail, name='book_view_detail'),
    path('book/<int:pk>/success', book_success, name='book_success'),

    path('event/list/', event_list, name='event_list'),
    path('event/detail/<int:pk>', panel_event_view_detail, name='panel_event_view_detail'),
    path('event/detail/', panel_event_post, name='panel_event_post'),
    path('event/<int:pk>/success', event_success, name='event_success'),
    path('event/orderer/<int:pk>', orderer_detail_view, name='orderer_detail_view'),
    path('event/orderer/', orderer_view, name='orderer_view'),

    # path('book/edit/', book_edit, name='book_edit'),
    path('customer/', customer_view, name='customer_view'),
    path('customer/detail/<int:pk>', customer_detail_view, name='customer_view_detail'),
]
