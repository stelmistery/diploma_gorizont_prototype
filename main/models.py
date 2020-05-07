from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    GENDERS = (
        ('m', 'Мужской'),
        ('f', 'Женский')
    )
    FIO = models.CharField(max_length=50, verbose_name='ФИО')
    organization = models.CharField(max_length=255, null=True, blank=True, verbose_name='Организация')
    place = models.CharField(max_length=255, null=True, blank=True, verbose_name='Должность')
    age = models.IntegerField(null=True, blank=True, verbose_name='Возраст')
    gender = models.CharField(max_length=1, choices=GENDERS, null=True, blank=True, verbose_name='Пол')
    phone = models.CharField(unique=True, max_length=20, null=False, verbose_name='Телефон')
    email = models.CharField(max_length=255, null=True, blank=True, verbose_name='Email')
    city = models.CharField(max_length=255, null=True, blank=True, verbose_name='Город')
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.FIO

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
