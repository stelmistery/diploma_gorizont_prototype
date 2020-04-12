from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    GENDERS = (
        ('m', 'male'),
        ('f', 'female')
    )
    middle_name = models.CharField(max_length=255, null=False, verbose_name='Отчество')
    organization = models.CharField(max_length=255, null=False, verbose_name='Организация')
    place = models.CharField(max_length=255, null=False, verbose_name='Должность')
    age = models.IntegerField(null=True, blank=False, verbose_name='Возраст')
    gender = models.CharField(max_length=1, choices=GENDERS, null=False, verbose_name='Пол')
    phone = models.CharField(max_length=20, null=False, verbose_name='Телефон')
    city = models.CharField(max_length=255, null=False, verbose_name='Город')


