from django.shortcuts import render
from book.services.booking_services import get_book_customer_all
# Create your views here.


def index(request):
    return render(request, 'panel/panel_base.html')


def orders(request):
    cbs = get_book_customer_all()
    context = {
        'cbs': cbs
    }
    return render(request, 'panel/orders.html', context)
