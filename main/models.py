from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    GENDERS = (
        ('m', 'male'),
        ('f', 'female')
    )
    first_name = models.CharField(max_length=50, null=True, blank=True, verbose_name='Имя')
    last_name = models.CharField(max_length=50, null=True, blank=True, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=50, null=True, blank=True, verbose_name='Отчество')
    organization = models.CharField(max_length=255, null=True, blank=True, verbose_name='Организация')
    place = models.CharField(max_length=255, null=True, blank=True, verbose_name='Должность')
    age = models.IntegerField(null=True, blank=True, verbose_name='Возраст')
    gender = models.CharField(max_length=1, choices=GENDERS, null=True, blank=True, verbose_name='Пол')
    phone = models.CharField(max_length=20, null=False, verbose_name='Телефон')
    city = models.CharField(max_length=255, null=True, blank=True, verbose_name='Город')
    passport = models.CharField(max_length=10, null=True, blank=True, verbose_name='Паспортные данные')
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)


