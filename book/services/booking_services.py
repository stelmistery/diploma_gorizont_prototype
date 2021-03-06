from book.models import Category, Room, Book, Customer
from django.db.models import Q


# Function for finding a free room for a given date (Room reservation subsystem)
def free_room_search_func(check_in_date, date_of_eviction, category, num):
    qr = (Q(book__check_in_date__lte=check_in_date) & Q(book__date_of_eviction__gte=check_in_date)) | \
         (Q(book__check_in_date__lte=date_of_eviction) & Q(book__date_of_eviction__gte=date_of_eviction)) | \
         (Q(book__check_in_date__lte=check_in_date) & Q(book__date_of_eviction__gte=date_of_eviction)) | \
         (Q(book__check_in_date__gte=check_in_date) & Q(book__date_of_eviction__lte=date_of_eviction))
    try:
        room = Room.objects.filter(category_id=category, number_of_place=num).exclude(qr).earliest('room_number')
    except Room.DoesNotExist:
        return False
    return room


def get_books_all():
    return Book.objects.all()


def get_book(pk):
    return Book.objects.get(pk=pk)


def get_customer(pk):
    return Customer.objects.get(pk=pk)


def del_session(request):
    del request.session['category']
    del request.session['phone']
    del request.session['number_of_adults']
    del request.session['number_of_children']
