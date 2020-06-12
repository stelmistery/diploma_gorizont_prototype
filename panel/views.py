from django.shortcuts import render, HttpResponseRedirect, redirect, reverse
from book.models import Book, Customer, Category
from event.models import Event
from django.views.generic.list import ListView
from .forms import PanelDataForm, PanelBookForm
from account.services import phone_converter
from book.services.booking_services import free_room_search_func, get_book
from django.contrib import messages


# Create your views here.


def index(request):
    return render(request, 'panel/panel_base.html')


class BookListView(ListView):
    template_name = 'panel/book_list.html'
    context_object_name = 'books'
    model = Book


#################################
# TODO: объелинить две функции
def book_view(request):
    if request.method == 'POST':
        pk = request.POST['pk']
        return redirect('/panel/book/detail/' + str(pk))
    return render(request, 'panel/book_view.html')


def book_view_detail(request, pk):
    try:
        book = get_book(pk)
    except:
        return render(request, 'panel/book_view.html', {'error': 'Такой брони нет'})
    return render(request, 'panel/book_view.html', {'book': book})


#################################


def customer_view(request):
    if request.method == 'POST':
        pk = request.POST['pk']
        return redirect('/panel/customer/detail/' + str(pk))
    return render(request, 'panel/customer_view.html')


# TODO: Доделать историю мероприятий
def customer_detail_view(request, pk):
    try:
        customer = Customer.objects.get(pk=pk)
    except:
        return render(request, 'panel/customer_view.html', {'error': 'Пользователь не найден'})
    books = Book.objects.filter(customer__phone=customer.phone)
    context = {
        'customer': customer,
        'books': books,
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

def book_create(request):
    if request.method == 'POST':
        pdf = PanelDataForm(request.POST)
        if pdf.is_valid():
            phone = phone_converter(pdf.cleaned_data.get('phone'))
            first_name = pdf.cleaned_data.get('first_name')
            last_name = pdf.cleaned_data.get('last_name')
            middle_name = pdf.cleaned_data.get('middle_name')
            email = pdf.cleaned_data.get('email')
            number_of_adults = pdf.cleaned_data.get('number_of_adults')
            number_of_children = pdf.cleaned_data.get('number_of_children')
            check_in = pdf.cleaned_data.get('check_in')
            departure = pdf.cleaned_data.get('departure')
            category = pdf.cleaned_data.get('category')
            additional_info = pdf.cleaned_data.get('additional_info')
            num = number_of_children + number_of_adults

            room = free_room_search_func(check_in, departure, category, num)

            if room:
                price = Category.objects.get(pk=room.category_id_id)
                price = (float(price.price) * number_of_adults) + (float(price.price) * number_of_children * 0.5)
                try:
                    customer = Customer.objects.create(first_name=first_name,
                                                       last_name=last_name,
                                                       middle_name=middle_name,
                                                       phone=phone, email=email)
                    book = Book.objects.create(room_id=room.pk,
                                               number_of_adults=number_of_adults,
                                               customer_id=customer.id,
                                               number_of_children=number_of_children,
                                               check_in_date=check_in,
                                               date_of_eviction=departure,
                                               additional_information=additional_info,
                                               price=price,
                                               confirmed=True)
                except:
                    pbf = PanelBookForm()
                    pdf = PanelDataForm()
                    context = {
                        'pdf': pdf,
                        'pbf': pbf
                    }
                    messages.success(request, 'Бронирование прошло успешно!')
                    return render(request, 'panel/book_create.html', context)

                pbf = PanelBookForm()
                pdf = PanelDataForm()
                context = {
                    'pdf': pdf,
                    'pbf': pbf
                }
                messages.success(request, 'Бронирование прошло успешно!')
                return render(request, 'panel/book_create.html', context)

    pbf = PanelBookForm()
    pdf = PanelDataForm()
    context = {
        'pdf': pdf,
        'pbf': pbf
    }
    return render(request, 'panel/book_create.html', context)


def book_check(request):
    if request.method == 'POST':
        pbf = PanelBookForm(request.POST)
        if pbf.is_valid():
            check_in = pbf.cleaned_data.get('check_in')
            departure = pbf.cleaned_data.get('departure')
            category = pbf.cleaned_data.get('category')
            number_of_adults = pbf.cleaned_data.get('number_of_adults')
            number_of_children = pbf.cleaned_data.get('number_of_children')
            num = number_of_adults + number_of_children

            room = free_room_search_func(check_in, departure, category, num)
            if room:
                pbf = PanelBookForm(initial={'check_in': check_in,
                                             'departure': departure,
                                             'category': category,
                                             'number_of_adults': number_of_adults,
                                             'number_of_children': number_of_children})

                pdf = PanelDataForm(initial={'check_in': check_in,
                                             'departure': departure,
                                             'category': category,
                                             'number_of_adults': number_of_adults,
                                             'number_of_children': number_of_children})
                context = {
                    'pdf': pdf,
                    'pbf': pbf
                }
                messages.info(request, 'Есть свободное место!')
                return render(request, 'panel/book_create.html', context)
            messages.warning(request, 'Что-то пошло не так')
            pbf = PanelBookForm()
            pdf = PanelDataForm()
            context = {
                'pdf': pdf,
                'pbf': pbf
            }
            return render(request, 'panel/book_create.html', context)
    pbf = PanelBookForm()
    pdf = PanelDataForm()
    context = {
        'pdf': pdf,
        'pbf': pbf
    }
    return render(request, 'panel/book_create.html', context)


def event_list(request):
    events = Event.objects.all()
    context = {'events': events}
    return render(request, 'panel/event_list.html', context)