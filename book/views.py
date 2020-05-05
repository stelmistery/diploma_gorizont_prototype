from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Category, Room, Book
from .forms import BookForm, DataForm
from .services.booking_services import free_room_search_func


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
                return HttpResponse(room)
            else:
                return HttpResponse('К сожалению свободные места на заданную дату отсутствуют. Вы можете выбрать /'
                                    ' другую дату или другую категорию')

    bookForm = BookForm()
    context = {'bookform': bookForm}
    return render(request, 'book/booking.html', context)
