from django.shortcuts import render, redirect, reverse, get_object_or_404, get_list_or_404
from django.http.response import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Event, Customer, Member
from .forms import EventForms
import pdb


def events(request):
    events = Event.objects.filter(status=True)
    return render(request, 'event/pub_event.html', {'events': events})


@login_required(login_url='/account/login/')
def save_event(request):
    print(request)
    f = EventForms()
    context = {'ef': f}
    return render(request, 'event/save_event.html', context)


@require_http_methods(['POST'])
def save_event_image(request):
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
    event.image = request.FILES['image']
    event.save()
    try:
        Member.objects.create(event=event, customer=customer, orderer=True)
    except:
        return HttpResponse('Сохранение Объекта member : неуспешно')
    # return render(request, 'main/index.html', {'event_done': 'Мероприятие отправлено на рассмотрение!'})
    # return HttpResponse('Сохранение Объекта member : тоже неуспешно')
    return HttpResponse('Сохранение Объекта member : все пашет')


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
