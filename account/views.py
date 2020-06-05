from django.shortcuts import render
from django.http.response import HttpResponse
from .forms import CustomerUserCreateForm
from django.contrib import messages
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LoginView
from .models import CustomerUser, PhoneOTP
from .services import send_otp
from .forms import CustomerUserCreateForm
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login


# def register(request):
#     if request.method == 'POST':
#         form = CustomerUserCreateForm(request.POST)
#         if form.is_valid():
#             form.save()
#     form = CustomerUserCreateForm()
#     return render(request, 'account/register.html', {'form': form})

#
# class RegisterUserView(CreateView):
#     model = CustomerUser
#     template_name = 'account/register.html'
#     form_class = CustomerUserCreateForm
#
#     def get_success_url(self):
#         return '/account/register/done'


def register_user(request):
    if request.method == 'POST':
        rf = CustomerUserCreateForm(request.POST)
        if rf.is_valid():
            cuser = CustomerUser.objects.filter(phone__iexact=rf.cleaned_data.get('phone'))
            if cuser.exists():
                error = 'Пользователь с таким телефоном уже зарегестрирован в системе'
                return render(request, 'account/register.html', context={'form': CustomerUserCreateForm,
                                                                         'errors': error})
            cuser = CustomerUser.objects.filter(email__iexact=rf.cleaned_data.get('email'))
            if cuser.exists():
                error = 'Пользователь с таким email уже зарегестрирован в системе'
                return render(request, 'account/register.html', context={'form': CustomerUserCreateForm,
                                                                         'errors': error})

            user = CustomerUser.objects.create_user(phone=rf.cleaned_data.get('phone'),
                                                    password=rf.cleaned_data.get('password1'),
                                                    email=rf.cleaned_data.get('email'))

            # error = 'Что-то пошло не так'
            # return HttpResponse(error)
            user = authenticate(request, phone=rf.cleaned_data.get('phone'), password=rf.cleaned_data.get('password1'))
            if user is not None:
                login(request, user)

            key = send_otp(rf.cleaned_data.get('phone'))
            phone = PhoneOTP.objects.create(phone=rf.cleaned_data.get('phone'), key=key)
    form = CustomerUserCreateForm
    context = {'form': form}
    return render(request, 'account/register.html', context)


class RegisterDoneView(TemplateView):
    template_name = 'account/register_done.html'


class LoginUserView(LoginView):
    template_name = 'account/login.html'
