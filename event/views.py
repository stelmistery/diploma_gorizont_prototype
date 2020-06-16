from django.shortcuts import render, redirect, reverse
from django.http.response import HttpResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Event, Customer, Member
from .forms import EventForms
import pdb


# @login_required(login_url='/account/login/')
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


