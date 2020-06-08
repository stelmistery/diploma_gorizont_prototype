from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Event, Customer, Member
from .forms import EventForms


@login_required(login_url='/account/login/')
def save_event(request):
    if request.method == 'POST':
        ef = EventForms(request.POST)
        if ef.is_valid():
            customer = request.user.customer
            event = ef.save()
            try:
                member = Member.objects.create(event=event, customer=customer)
            except:
                return HttpResponse('Сохранение Объекта member : неуспешно')
            return render(request, 'main/index.html', {'event_done': 'Меропряитие отправлено на рассмотрение!'})
    ef = EventForms()
    context = {'ef': ef}
    return render(request, 'event/save_event.html', context)