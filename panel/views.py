from django.shortcuts import render
from book.models import Book, Customer_Book, Customer
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from book.services.booking_services import get_book_customer_all
# Create your views here.


def index(request):
    return render(request, 'panel/panel_base.html')


class BookListView(ListView):
    template_name = 'panel/book_list.html'
    context_object_name = 'cbs'

    def get_queryset(self):
        return Customer_Book.objects.all()


class BookDetailView(DetailView):
    model = Customer_Book
    context_object_name = 'cb'
    template_name = 'panel/book_view.html'
