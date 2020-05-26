from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from .services import phone_converter


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, phone, email, password):
        """
        Create and save a User with the given email and password.
        """
        if not phone:
            raise ValueError(_('Номер телефона должен присутсовать'))
        if not email:
            raise ValueError(_('Email должен присутствовать'))

        user = self.model(email=self.normalize_email(email),
                          phone=phone_converter(phone))

        user.set_password(password)
        user.save(using=self._db)
        return user

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
