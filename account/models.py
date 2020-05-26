from django.db import models
from .managers import CustomUserManager
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from .validators import validate_phone_number
from django.conf import settings


class CustomerUser(AbstractUser):
    first_name = None
    last_name = None
    username = None
    phone = models.CharField(max_length=15, validators=[validate_phone_number], unique=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    def __str__(self):
        return self.email


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
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.last_name + ' ' + self.first_name + ' ' + self.middle_name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
