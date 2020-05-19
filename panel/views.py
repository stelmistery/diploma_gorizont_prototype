from django.shortcuts import render, HttpResponseRedirect
from book.models import Book, Customer_Book, Customer
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from book.services.booking_services import get_book_customer_all


# Create your views here.


def index(request):
    return render(request, 'panel/panel_base.html')


class BookListView(ListView):
    paginate_by = 20
    template_name = 'panel/book_list.html'
    context_object_name = 'cbs'

    def get_queryset(self):
        return Customer_Book.objects.all()


#################################
# TODO: объелинить две функции
def book_view(request):
    if request.method == 'POST':
        pk = request.POST['pk']
        try:
            cb = Customer_Book.objects.get(book_id_id=pk)
        except:
            return render(request, 'panel/book_view.html', {'error': 'Такой брони нет'})
        return render(request, 'panel/book_view.html', {'cb': cb})
    return render(request, 'panel/book_view.html')


def book_view_detail(request, pk):
    try:
        cb = Customer_Book.objects.get(book_id_id=pk)
    except:
        return render(request, 'panel/book_view.html', {'error': 'Такой брони нет'})
    return render(request, 'panel/book_view.html', {'cb': cb})
#################################


# TODO: Дописать класс просмотря профиля
class CustomerDetailView(DetailView):
    pass


# TODO:Дописать функцию подтверждения бронирования со стороны менеджера
def book_success(request, pk):
    Book.objects.filter(pk=pk).update(confirmed=True)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
