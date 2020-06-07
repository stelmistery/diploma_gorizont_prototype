from django.shortcuts import render
from django.http.response import HttpResponse
from .forms import PhoneValid
from .models import PhoneOTP
from .services import send_otp

class PhoneValidMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.user.is_authenticated:
            user = request.user
            if not user.is_staff:
                key = send_otp(user.phone)
                if key:
                    phone = PhoneOTP.objects.create(phone=user.phone, otp=key)
                    code_form = PhoneValid(initial={'phone': user.phone})
                    return render(request, 'account/register.html',
                                  context={'phone_field': code_form, 'phone': user.phone})
                else:
                    return HttpResponse('что-то пошло не так 2')


