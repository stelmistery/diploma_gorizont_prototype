from django.shortcuts import render
from django.http.response import HttpResponse
from .forms import CustomerUserCreateForm
from django.contrib import messages
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LoginView
from .models import CustomerUser, PhoneOTP
from .services import send_otp
from .forms import CustomerUserCreateForm, PhoneValid
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
            filt_user = CustomerUser.objects.filter(phone__iexact=rf.cleaned_data.get('phone'))
            if filt_user.exists():
                error = 'Пользователь с таким телефоном уже зарегестрирован в системе'
                return render(request, 'account/register.html', context={'form': CustomerUserCreateForm,
                                                                         'errors': error})
            filt_user = CustomerUser.objects.filter(email__iexact=rf.cleaned_data.get('email'))
            if filt_user.exists():
                error = 'Пользователь с таким email уже зарегестрирован в системе'
                return render(request, 'account/register.html', context={'form': CustomerUserCreateForm,
                                                                         'errors': error})
            try:
                user = CustomerUser.objects.create_user(phone=rf.cleaned_data.get('phone'),
                                                        password=rf.cleaned_data.get('password1'),
                                                        email=rf.cleaned_data.get('email'))
            except:
                error = 'Что-то пошло не так 1'
                return HttpResponse(error)
            auth_user = authenticate(request, phone=rf.cleaned_data.get('phone'), password=rf.cleaned_data.get('password1'))
            if auth_user is not None:
                login(request, auth_user)

            key = send_otp(user.phone)
            if key:
                try:
                    phone = PhoneOTP.objects.get(phone=user.phone)
                    phone.otp = key
                except:
                    phone = PhoneOTP.objects.create(phone=user.phone, otp=key)
                code_form = PhoneValid(initial={'phone': user.phone})
                return render(request, 'account/register.html', context={'phone_field': code_form, 'phone': user.phone})
            else:
                return HttpResponse('что-то пошло не так 2')
    form = CustomerUserCreateForm
    context = {'form': form}
    return render(request, 'account/register.html', context)


def phone_activate(request):
    if request.method == 'POST':
        pa = PhoneValid(request.POST)
        if pa.is_valid():
            if request.user.phone == pa.cleaned_data.get('phone'):
                phone_otp = PhoneOTP.objects.get(phone=pa.cleaned_data.get('phone'))
                if phone_otp:
                    if phone_otp.otp == pa.cleaned_data.get('code'):
                        user_id = request.user.id
                        user = CustomerUser.objects.get(pk=user_id)
                        user.is_staff = True
                        user.save()
        return redirect('/')


class RegisterDoneView(TemplateView):
    template_name = 'account/register_done.html'


class LoginUserView(LoginView):
    template_name = 'account/login.html'
