from django.db import models
from account.models import Customer
from django.core.validators import MaxValueValidator


class Category(models.Model):
    name = models.CharField(max_length=255, null=False, verbose_name='Название')
    conditions = models.TextField(null=False, verbose_name='Условия')
    price = models.IntegerField(null=False, verbose_name='Цена')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['price']


class Room(models.Model):
    room_number = models.CharField(primary_key=True, max_length=5, verbose_name='Номер комнаты')
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Номер категории')
    number_of_place = models.IntegerField(null=False, verbose_name='Кол-во мест')

    def __str__(self):
        return self.room_number + '_' + self.category_id.name + '_' + str(self.number_of_place)

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Команты'
        ordering = ['room_number']


class Book(models.Model):
    Book_code = models.AutoField(primary_key=True, verbose_name='Код брони')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='Номер комнаты')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Клиент')
    number_of_adults = models.IntegerField(verbose_name='Кол-во взрослых', default=0, validators=[MaxValueValidator(4)])
    number_of_children = models.IntegerField(verbose_name='Кол-во детей', default=0, validators=[MaxValueValidator(4)])
    check_in_date = models.DateField(verbose_name='Дата заселения')
    date_of_eviction = models.DateField(verbose_name='Дата выселения')
    additional_information = models.TextField(verbose_name='Дополнительная информация', null=True, blank=True)
    price = models.FloatField(verbose_name='Сумма', default=0)
    confirmed = models.BooleanField(default=False, verbose_name='Подтвержедено')

    def __str__(self):
        return str(self.Book_code)

    class Meta:
        verbose_name = 'Бронь'
        verbose_name_plural = 'Брони'
