from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from .validators import validate_phone_number
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager
from .services import phone_converter



class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, phone, email, password, first_name='-', last_name='-', middle_name='-'):
        """
        Create and save a User with the given email and password.
        """
        if not phone:
            raise ValueError(_('Номер телефона должен присутсовать'))
        if not email:
            raise ValueError(_('Email должен присутствовать'))

        customer = Customer.objects.create(phone=phone,
                                           email=email,
                                           first_name=first_name,
                                           last_name=last_name,
                                           middle_name=middle_name)

        user = self.model(email=self.normalize_email(email),
                          phone=phone_converter(phone))

        user.customer_id = customer.pk
        user.is_staff = False
        user.set_password(password)
        user.save(using=self._db)
        return user

    # def create_staffuser(slef, phone, password, email):
    #     user = self.create_user()

    def create_superuser(self, phone, email, password):
        """
        Create and save a SuperUser with the given email and password.
        """
        user = self.create_user(email=self.normalize_email(email),
                                password=password,
                                phone=phone_converter(phone))

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Customer(models.Model):
    GENDERS = (
        ('m', 'Мужской'),
        ('f', 'Женский')
    )
    first_name = models.CharField(max_length=50, verbose_name='Имя', default='-')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия', default='-')
    middle_name = models.CharField(max_length=50, verbose_name='Отчество', default='-')
    organization = models.CharField(max_length=255, null=True, blank=True, verbose_name='Организация')
    place = models.CharField(max_length=255, null=True, blank=True, verbose_name='Должность')
    data_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDERS, null=True, blank=True, verbose_name='Пол')
    phone = models.CharField(max_length=20, validators=[validate_phone_number], null=False, verbose_name='Телефон')
    email = models.CharField(max_length=255, null=True, blank=True, verbose_name='Email')
    city = models.CharField(max_length=255, null=True, blank=True, verbose_name='Город')

    # user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.last_name + ' ' + self.first_name + ' ' + self.middle_name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class CustomerUser(AbstractUser):
    first_name = None
    last_name = None
    username = None
    is_staff = models.BooleanField(default=False)
    phone = models.CharField(_('Номер телефона'),
                             max_length=15,
                             validators=[validate_phone_number],
                             unique=True,
                             error_messages={
                                 'unique': _("Пользователь с таким номером уже сущесвтует"), })

    email = models.EmailField(_('Email'),
                              unique=True,
                              error_messages={
                                  'unique': _("Пользователь с таким email уже сущесвтует"), })
    customer = models.OneToOneField(Customer, verbose_name='Клиент', on_delete=models.CASCADE, unique=True,
                                    error_messages={'unique': _('Такой клиент уже привязан к пользователю')})
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def get_phone(self):
        return self.phone


class PhoneOTP(models.Model):
    phone = models.CharField(validators=[validate_phone_number], max_length=15, unique=True)
    otp = models.CharField(max_length=9, blank=True, null=True)
    count = models.IntegerField(default=0, help_text='Кол-во отправленных сообщений')

    def __str__(self):
        return str(self.phone) + ' отправлено ' + self.otp
