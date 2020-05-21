from django.shortcuts import render, HttpResponseRedirect, redirect, reverse
from book.models import Book, Customer_Book, Customer
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from book.services.booking_services import get_book_customer_all, get_book_customer
from book.forms import BookForm, DataForm


# Create your views here.


def index(request):
    return render(request, 'panel/panel_base.html')


class BookListView(ListView):
    template_name = 'panel/book_list.html'
    context_object_name = 'cbs'

    def get_queryset(self):
        return Customer_Book.objects.all()


#################################
# TODO: объелинить две функции
def book_view(request):
    if request.method == 'POST':
        pk = request.POST['pk']
        return redirect('/panel/book/detail/' + str(pk))
    return render(request, 'panel/book_view.html')


def book_view_detail(request, pk):
    try:
        cb = get_book_customer(pk)
    except:
        return render(request, 'panel/book_view.html', {'error': 'Такой брони нет'})
    return render(request, 'panel/book_view.html', {'cb': cb})


#################################


# class CustomerDetailView(DetailView):
#     template_name = 'panel/customer_view.html'
#     model = Customer
#     context_object_name = 'cust'


def customer_detail_view(request, pk):
    try:
        cust = Customer.objects.get(pk=pk)
    except:
        return render(request, 'panel/book_view.html', {'error': 'Пользователь не найден'})
    cbs = Customer_Book.objects.filter(customer_id__phone=cust.phone)
    context = {
        'cbs': cbs,
        'cust': cust,
    }
    return render(request, 'panel/customer_view.html', context)


def book_success(request, pk):
    Book.objects.filter(pk=pk).update(confirmed=True)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


# def book_edit(request):
#     if request.method == 'POST':
#         if request.POST['pk']:
#             pk = request.POST['pk']
#             try:
#                 cb = get_book_customer(pk)
#             except:
#                 return render(request, 'panel/book_edit.html', {'error': 'Такой брони нет'})
#             request.session['book_pk'] = cb.book_id.id
#             request.session['customer_pk'] = cb.customer_id.id
#             initial = {
#                 'check_in_date': cb.book_id.check_in_date,
#                 'date_of_eviction': cb.book_id.date_of_eviction,
#                 'category': cb.book_id.room_id.category_id,
#                 'number_of_adults': cb.book_id.number_of_adults,
#                 'number_of_children': cb.book_id.number_of_children,
#                 'first_name': cb.customer_id.first_name,
#                 'last_name': cb.customer_id.last_name,
#                 'middle_name': cb.customer_id.middle_name,
#                 'phone': cb.customer_id.phone,
#                 'email': cb.customer_id.email,
#                 'additional_info': cb.book_id.additional_information
#             }
#             df = DataForm(initial=initial)
#             return render(request, 'panel/book_edit.html', {'cb': cb, 'df': df})
#
#         df = DataForm(request.POST)
#         if df.is_valid():
#
#             book = Book.objects.get(pk=request.session['book_pk'])
#
#
#
#     return render(request, 'panel/book_edit.html')
