from django.shortcuts import render, HttpResponseRedirect, redirect, reverse, get_list_or_404, HttpResponse
from book.models import Book, Category
from account.models import CustomerUser, Customer
from event.models import Event, Member
from event.forms import EventForms
from django.views.decorators.http import require_http_methods
from django.views.generic.list import ListView
from django.db.models import Q
from .forms import PanelDataForm, PanelBookForm
from account.services import phone_converter
from book.services.booking_services import free_room_search_func, get_book
from event.models import get_event
from django.contrib import messages
import pdb
from django.contrib.auth.models import Group


###################### ----> TODO_LIST <---- ######################
# TODO: Доделать иконки на панели
# TODO: Перевести элементы таблицы с сортировкой на русский язык

###################### ----> END TODO_LIST <---- ######################

# Create your views here.

###################### ----> BOOK <---- ######################
def index(request):
    return render(request, 'panel/panel_base.html')


class BookListView(ListView):
    template_name = 'panel/book_list.html'
    context_object_name = 'books'
    model = Book


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


def customer_view(request):
    if request.method == 'POST':
        pk = request.POST['pk']
        return redirect('/panel/customer/detail/' + str(pk))
    return render(request, 'panel/customer_view.html')


def customer_detail_view(request, pk):
    # pdb.set_trace()
    try:
        customer = Customer.objects.get(pk=pk)
    except:
        return render(request, 'panel/customer_view.html', {'error': 'Пользователь не найден'})
    books = Book.objects.filter(customer__phone=customer.phone)
    events = Event.objects.filter(member__customer_id=customer.id)
    reg_status = CustomerUser.objects.filter(customer_id=customer.id)
    if reg_status:
        reg_status = True
    else:
        reg_status = False
    context = {
        'customer': customer,
        'books': books,
        'events': events,
        'reg_status': reg_status
    }
    return render(request, 'panel/customer_view.html', context)


def book_success(request, pk):
    Book.objects.filter(pk=pk).update(confirmed=True)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


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


###################### ----> END BOOK <---- ######################


###################### ----> EVENT <---- ######################
def panel_event_post(request):
    if request.method == 'POST':
        pk = request.POST['pk']
        return redirect('/panel/event/detail/' + str(pk))
    return render(request, 'panel/event_view.html')


def event_list(request):
    events = Event.objects.all()
    context = {'events': events}
    return render(request, 'panel/event_list.html', context)


def panel_event_view_detail(request, pk):
    try:
        event = get_event(pk)
        # qr = (Q(pk=Member.customer.pk) & Q())
        orderer = Customer.objects.filter(member__orderer=True).filter(member__event=event).first()

    except:
        return render(request, 'panel/event_view.html', {'error': 'Такого мероприятия нет'})
    return render(request, 'panel/event_view.html', {'event': event, 'orderer': orderer})


def event_success(request, pk):
    Event.objects.filter(pk=pk).update(status=True)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def orderer_view(request):
    if request.method == 'POST':
        pk = request.POST['pk']
        return redirect('/panel/event/orderer/' + str(pk))
    return render(request, 'panel/orderer_viev.html')


def orderer_detail_view(request, pk):
    customer = Customer.objects.filter(pk=pk).filter(member__orderer=True).first()
    if customer is not None:
        books = Book.objects.filter(customer__phone=customer.phone)
        events = Event.objects.filter(member__customer_id=customer.id)
        reg_status = CustomerUser.objects.filter(customer_id=customer.id)
        if reg_status:
            reg_status = True
        else:
            reg_status = False
        context = {
            'customer': customer,
            'books': books,
            'events': events,
            'reg_status': reg_status
        }
        return render(request, 'panel/orderer_viev.html', context)
    return render(request, 'panel/orderer_viev.html', {'error': 'Такого заказчика нет'})


def member_list_view(request, pk):
    members = get_list_or_404(Member, event_id=pk)
    return render(request, 'panel/list_member.html', {'members': members})


# TODO: Доделать html
def create_event(request):
    if request.method == 'POST':
        event = Event()
        # pdb.set_trace()
        event.image = request.FILES['image']
        customer = request.user.customer
        event.name = request.POST['name']
        event.type = request.POST['type']
        event.description = request.POST['description']
        event.cost = request.POST['cost']
        event.start_date = request.POST['start_date']
        event.end_date = request.POST['end_date']
        event.max_members = request.POST['max_members']
        event.tech_support = request.POST['tech_support']
        event.save()
        try:
            Member.objects.create(event=event, customer=customer, orderer=True)
        except:
            return HttpResponse('Сохранение Объекта event : неуспешно')
        return HttpResponse('Сохранение Объекта member : все пашет')
    ef = EventForms()
    return render(request, 'panel/create_event.html', {'ef': ef})


###################### ----> END EVENT <---- ######################


###################### ----> MANAGER SETTIGNS <---- ######################

def manager_list(request):
    managers = CustomerUser.objects.filter(is_staff=True)
    context = {
        'managers': managers
    }
    return render(request, 'panel/manager_list.html', context)


def group_list(request):
    groups = Group.objects.all()
    context = {
        'groups': groups
    }
    return render(request, 'panel/group_list.html', context)


@require_http_methods(["POST"])
def add_group(request):
    name = request.POST.get('name')
    if Group.objects.filter(name=name).exists():
        messages.warning(request, 'Группа с таким названием уже существует')
        return redirect('group_list')
    else:
        group = Group()
        group.name = name
        group.save()
        return redirect('group_list')


def del_group(request, pk):
    group = Group.objects.get(pk=pk)
    group.delete()
    return redirect('group_list')


def manager_group(request, pk):
    customer = CustomerUser.objects.get(pk=pk)
    ugroups = customer.groups.all()
    groups = Group.objects.exclude(id__in=ugroups)
    context = {
        'groups': groups,
        'customer': customer,
        'ugroups': ugroups
    }
    return render(request, 'panel/manager_group.html', context)

#
# def manager_group_add(request, pk):
#     customer = CustomerUser.objects.get(pk=pk)
#     ugroups = customer.groups.all()
#     groups = Group.objects.exclude(pk=ugroups.pk)
#
#     context = {
#         'groups': groups,
#         'customer': customer,
#         'ugroups': ugroups
#     }
#     return render(request, 'panel/manager_group.html', context)

###################### ----> END MANAGER SETTIGNS <---- ######################
