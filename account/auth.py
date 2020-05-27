from django.contrib.auth import get_user_model
from django.contrib.auth import backends, get_user_model
from django.db.models import Q


class AuthenticationBackend(backends.ModelBackend):
    """
    Custom authentication Backend for login using email,phone,username
    with password
    """


def authenticate(self, username=None, password=None, **kwargs):
    usermodel = get_user_model()
    try:
        user = usermodel.objects.get(
            Q(email__iexact=username) | Q(phone__iexact=username))

        if user.check_password(password):
            return user
    except usermodel.DoesNotExist:
        pass
