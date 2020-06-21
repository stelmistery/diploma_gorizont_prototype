from django.db import models
from account.models import Customer


class Event(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    type = models.CharField(max_length=50, verbose_name='Тип мероприятия')
    description = models.TextField(verbose_name='Описание мероприятия')
    image = models.ImageField(upload_to='images/')
    cost = models.FloatField(verbose_name='Стоимость участия', default=0, blank=True, null=True)
    start_date = models.DateTimeField(verbose_name='Дата начала проведения')
    end_date = models.DateTimeField(verbose_name='Дата окончания проведения')
    max_members = models.IntegerField(blank=True, null=True, verbose_name='Макс. кол-во участников')
    tech_support = models.TextField(blank=True, null=True, verbose_name='Техническое сопровождение')
    status = models.BooleanField(default=0, verbose_name='Статус')
    create_date = models.DateTimeField(auto_now_add=True)
    pub_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name + ': ' + self.type

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'
        ordering = ['start_date']


def get_event(pk):
    return Event.objects.get(pk=pk)


class Member(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Клиент')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name='Мероприятие')
    orderer = models.BooleanField(verbose_name='Заказчик', default=0)

    def __str__(self):
        return str(self.event) + ' ' + str(self.customer)

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'