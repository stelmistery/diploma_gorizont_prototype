from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import Room, Book, Customer, Customer_Book
from .forms import BookForm, DataForm
from .services.booking_services import free_room_search_func
import datetime


# from formtools.wizard.views import SessionWizardView


def room_check(request):
    if request.method == 'POST':
        bf = BookForm(request.POST)
        if bf.is_valid():
            check_in_date = bf.cleaned_data['check_in_date']
            date_of_eviction = bf.cleaned_data['date_of_eviction']
            category = bf.cleaned_data['category']
            number_of_adults = int(bf.cleaned_data['number_of_adults'])
            number_of_children = int(bf.cleaned_data['number_of_children'])
            num = number_of_adults + number_of_children

            room = free_room_search_func(check_in_date, date_of_eviction, category, num)
            request.session['room'] = room.pk

            if room:
                request.session['category'] = category.pk
                initial = {'check_in_date': check_in_date,
                           'date_of_eviction': date_of_eviction,
                           'category': category,
                           'number_of_adults': number_of_adults,
                           'number_of_children': number_of_children}

                df = DataForm(initial=initial)

                context = {'df': df, 'category': category}
                return render(request, 'book/bookproc.html', context)
            else:
                return HttpResponse('К сожалению свободные места на заданную дату отсутствуют. Вы можете выбрать /'
                                    ' другую дату или другую категорию')

    bf = BookForm()
    context = {'bookform': bf}
    return render(request, 'book/booking.html', context)


def book_process(request):
    if request.method == 'POST':
        df = DataForm(request.POST)
        bf = BookForm(request.POST)
        if bf.is_valid() and df.is_valid():
            check_in_date = bf.cleaned_data['check_in_date']
            date_of_eviction = bf.cleaned_data['date_of_eviction']
            category = bf.cleaned_data['category']
            number_of_adults = int(bf.cleaned_data['number_of_adults'])
            number_of_children = int(bf.cleaned_data['number_of_children'])
            num = number_of_adults + number_of_children

            fio = df.cleaned_data['fio']
            phone = df.cleaned_data['phone']
            email = df.cleaned_data['email']

            additional_info = request.POST.get('additional_info')

            request.session['check_in_date_year'] = check_in_date.year
            request.session['check_in_date_month'] = check_in_date.month
            request.session['check_in_date_day'] = check_in_date.day
            request.session['date_of_eviction_year'] = date_of_eviction.year
            request.session['date_of_eviction_month'] = date_of_eviction.month
            request.session['date_of_eviction_day'] = date_of_eviction.day
            request.session['category'] = category.pk
            request.session['number_of_adults'] = number_of_adults
            request.session['number_of_children'] = number_of_children
            request.session['fio'] = fio
            request.session['phone'] = phone
            request.session['email'] = email
            request.session['additional_info'] = additional_info

            context = {'check_in_date': check_in_date,
                       'date_of_eviction': date_of_eviction,
                       'category': category,
                       'number_of_adults': number_of_adults,
                       'number_of_children': number_of_children,
                       'fio': fio,
                       'phone': phone,
                       'email': email,
                       'additional_info': additional_info}

            return render(request, 'book/confirmed.html', context)


def book_confirmed(request):
    if request.method == 'POST':
        check_in_date_year = request.session['check_in_date_year']
        check_in_date_month = request.session['check_in_date_month']
        check_in_date_day = request.session['check_in_date_day']
        date_of_eviction_year = request.session['date_of_eviction_year']
        date_of_eviction_month = request.session['date_of_eviction_month']
        date_of_eviction_day = request.session['date_of_eviction_day']
        category_pk = request.session['category']
        number_of_adults = request.session['number_of_adults']
        number_of_children = request.session['number_of_children']
        fio = request.session['fio']
        phone = request.session['phone']
        email = request.session['email']
        additional_info = request.session['additional_info']
        room = request.session['room']
        num = number_of_children + number_of_adults
        check_in_date = datetime.datetime(check_in_date_year, check_in_date_month, check_in_date_day)
        date_of_eviction = datetime.datetime(date_of_eviction_year, date_of_eviction_month, date_of_eviction_day)

        customer = Customer.objects.create(FIO=fio, phone=phone, email=email)
        book = Book.objects.create(room_id_id=room, number_of_people=num, check_in_date=check_in_date,
                                   date_of_eviction=date_of_eviction, confirmed=False)

        cb = Customer_Book.objects.create(customer_id_id=customer.pk, book_id_id=book.pk)
        if cb.pk:
            return HttpResponse('Поздравляю, это ваша бронь: ' + str(cb.pk))
        else:
            return HttpResponse('Брони нема, ибо руки из жопы Рикардо Милоса')