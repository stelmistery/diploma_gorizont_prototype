from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import Room, Book, Category
from account.models import Customer
from .forms import BookForm, DataForm, AuthDataForm
from .services.booking_services import free_room_search_func, del_session
from account.services import phone_converter
import datetime


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

            if room:
                if request.user.is_authenticated:
                    user = request.user.customer_id
                    customer_user = Customer.objects.get(id=user)
                    initial = {'check_in_date': check_in_date,
                               'date_of_eviction': date_of_eviction,
                               'category': category,
                               'number_of_adults': number_of_adults,
                               'number_of_children': number_of_children,
                               'first_name': customer_user.first_name,
                               'last_name': customer_user.last_name,
                               'middle_name': customer_user.middle_name,
                               'phone': customer_user.phone,
                               'email': customer_user.email}

                    df = AuthDataForm(initial=initial)
                else:
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
        else:
            return HttpResponse('Данные введены не корректно')

    bf = BookForm()
    context = {'bookform': bf}
    return render(request, 'book/booking.html', context)


def book_process(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            df = AuthDataForm(request.POST)
            print('проверка на пользователя проходит')
        else:
            df = DataForm(request.POST)
        if df.is_valid():
            check_in_date = df.cleaned_data['check_in_date']
            date_of_eviction = df.cleaned_data['date_of_eviction']
            category = df.cleaned_data['category']
            number_of_adults = int(df.cleaned_data['number_of_adults'])
            number_of_children = int(df.cleaned_data['number_of_children'])
            num = number_of_adults + number_of_children
            first_name = df.cleaned_data['first_name']
            last_name = df.cleaned_data['last_name']
            middle_name = df.cleaned_data['middle_name']
            phone = phone_converter(df.cleaned_data['phone'])
            email = df.cleaned_data['email']
            additional_info = df.cleaned_data['additional_info']

            room = free_room_search_func(check_in_date, date_of_eviction, category, num)

            price = Category.objects.get(pk=room.category_id_id)
            price = (float(price.price) * number_of_adults) + (float(price.price) * number_of_children * 0.5)

            if room:
                check_in_date_str = check_in_date.strftime('%m/%d/%Y')
                date_of_eviction_str = date_of_eviction.strftime('%m/%d/%Y')

                request.session['check_in_date_str'] = check_in_date_str
                request.session['date_of_eviction_str'] = date_of_eviction_str
                request.session['category'] = category.pk
                request.session['number_of_adults'] = number_of_adults
                request.session['number_of_children'] = number_of_children
                request.session['first_name'] = first_name
                request.session['last_name'] = last_name
                request.session['middle_name'] = middle_name
                request.session['phone'] = phone
                request.session['email'] = email
                request.session['price'] = price
                request.session['additional_info'] = additional_info

                context = {'check_in_date': check_in_date,
                           'date_of_eviction': date_of_eviction,
                           'category': category,
                           'number_of_adults': number_of_adults,
                           'number_of_children': number_of_children,
                           'first_name': first_name,
                           'last_name': last_name,
                           'middle_name': middle_name,
                           'phone': phone,
                           'email': email,
                           'price': price,
                           'additional_info': additional_info}

                return render(request, 'book/confirmed.html', context)
            return HttpResponse('Кажется, мест в данной категории нет')
        return HttpResponse('Некорректные данные')
    return HttpResponse('Выбере категорию для бронирования')


def book_confirmed(request):
    if request.method == 'POST':
        try:
            check_in_date = datetime.datetime.strptime(request.session['check_in_date_str'], '%m/%d/%Y')
            date_of_eviction = datetime.datetime.strptime(request.session['date_of_eviction_str'], '%m/%d/%Y')
            number_of_adults = request.session['number_of_adults']
            number_of_children = request.session['number_of_children']
            category = request.session['category']
            first_name = request.session['first_name']
            last_name = request.session['last_name']
            middle_name = request.session['middle_name']
            phone = request.session['phone']
            email = request.session['email']
            additional_info = request.session['additional_info']
            price = request.session['price']
            num = number_of_children + number_of_adults
        except:
            return HttpResponse('Что-то пошло не так. Попробуйте выполнить процесс бронирования ещё раз')

        room = free_room_search_func(check_in_date, date_of_eviction, category, num)

        if room:
            customer = Customer.objects.create(first_name=first_name,
                                               last_name=last_name,
                                               middle_name=middle_name,
                                               phone=phone, email=email)
            book = Book.objects.create(room_id=room.pk,
                                       number_of_adults=number_of_adults,
                                       customer_id=customer.id,
                                       number_of_children=number_of_children,
                                       check_in_date=check_in_date,
                                       date_of_eviction=date_of_eviction,
                                       additional_information=additional_info,
                                       price=price,
                                       confirmed=False)

            if book.pk:
                del_session(request)
                return HttpResponse('Поздравляю, это ваша бронь: ' + str(book.pk))
            else:
                del_session(request)
                book.delete()
                return HttpResponse('Брони нема, ибо руки из жопы Рикардо Милоса')
        else:
            del_session(request)
            return HttpResponse('К сожалению, по вашим критериям все комнаты заняты')
    del_session(request)
    return HttpResponse('Заполните поля для бронирования')
