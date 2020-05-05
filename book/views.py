from django.shortcuts import render
from django .http.response import HttpResponse
from .models import Category, Room, Book
from .forms import BookForm, DataForm
import datetime
from django.http import JsonResponse
from django.db.models import Q


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

            qr = (Q(book__check_in_date__lte=check_in_date) & Q(book__date_of_eviction__gte=check_in_date)) | \
                (Q(book__check_in_date__lte=date_of_eviction) & Q(book__date_of_eviction__gte=date_of_eviction)) | \
                (Q(book__check_in_date__lte=check_in_date) & Q(book__date_of_eviction__gte=date_of_eviction)) | \
                (Q(book__check_in_date__gte=check_in_date) & Q(book__date_of_eviction__lte=date_of_eviction))
            rooms = Room.objects.filter(category_id=category, number_of_place=num).exclude(qr)

            return HttpResponse(rooms)

    bookForm = BookForm()
    context = {'bookform': bookForm}
    return render(request, 'book/booking.html', context)


# def booking_procedure(request):
#
#     check_in_date = request.POST.get('check_in_date')
#     date_of_eviction = request.POST.get('date_of_eviction')
#     category = request.POST.get('category')
#     number_of_adults = request.POST.get('number_of_adults')
#     number_of_children = request.POST.get('number_of_children')
#
#     bookForm = BookForm(initial={'check_in_date': check_in_date})
#     dataForm = DataForm()
#
#
#
#     return HttpResponse('def data_confirmation')
#
#
# def data_confirmation(request):
#     return HttpResponse('def data_confirmation')
