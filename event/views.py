from django.shortcuts import render, redirect, reverse, get_object_or_404, get_list_or_404
from django.http.response import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Event, Customer, Member
from .forms import EventForms
from django.core.mail import send_mail
import pdb


def events(request):
    events = Event.objects.filter(status=True)
    return render(request, 'event/pub_event.html', {'events': events})


#
# @login_required(login_url='/account/login/')
# def save_event(request):
#     print(request)
#     f = EventForms()
#     context = {'ef': f}
#     return render(request, 'event/save_event.html', context)


# @require_http_methods(['POST'])
def save_event(request):
    f = EventForms()
    if request.method == 'POST':
        f = EventForms(request.POST, request.FILES)
        if f.is_valid():
            event = Event()
            try:
                customer = request.user.customer
                event = Event.objects.create(
                    image=f.cleaned_data.get('image'),
                    name=f.cleaned_data.get('name'),
                    type=f.cleaned_data.get('type'),
                    description=f.cleaned_data.get('description'),
                    cost=f.cleaned_data.get('cost'),
                    start_date=f.cleaned_data.get('start_date'),
                    end_date=f.cleaned_data.get('end_date'),
                    max_members=f.cleaned_data.get('max_members'),
                    tech_support=f.cleaned_data.get('tech_support')
                )
                Member.objects.create(event=event, customer=customer, orderer=True)
            except:
                return HttpResponse('Сохранение Объекта member : неуспешно')
            start_date = f.cleaned_data.get('start_date').strftime('%m/%d/%Y')
            end_date = f.cleaned_data.get('end_date').strftime('%m/%d/%Y')
            send_mail('Мероприятие: ' + request.POST['name'], request.POST['description'] + 'Дата прведения от ' +
                      start_date + ' по ' + end_date,
                      from_email='stelmistery@yandex.ru',
                      recipient_list=['stelmistery@yandex.ru'])
            return HttpResponse('Ваша заявка отправлена на рассмотрение')
    context = {'ef': f}
    return render(request, 'event/save_event.html', context)


def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    memvers = get_list_or_404(Member, event=event)
    return render(request, 'event/event_detail.html', {'event': event, 'members': memvers})


@login_required(login_url='/account/login/')
def participate(request, pk, user_id):
    member = Member()
    member.event_id = pk
    member.customer_id = user_id
    member.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
