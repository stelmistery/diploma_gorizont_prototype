from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    GENDERS = (
        ('m', 'Мужской'),
        ('f', 'Женский')
    )
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=50, verbose_name='Отчество')
    organization = models.CharField(max_length=255, null=True, blank=True, verbose_name='Организация')
    place = models.CharField(max_length=255, null=True, blank=True, verbose_name='Должность')
    data_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDERS, null=True, blank=True, verbose_name='Пол')
    phone = models.CharField(max_length=20, null=False, verbose_name='Телефон')
    email = models.CharField(max_length=255, null=True, blank=True, verbose_name='Email')
    city = models.CharField(max_length=255, null=True, blank=True, verbose_name='Город')
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.last_name + ' ' + self.first_name + ' ' + self.middle_name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
