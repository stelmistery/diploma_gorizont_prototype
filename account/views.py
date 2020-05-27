from django.shortcuts import render
from .forms import CustomerUserCreateForm
from django.contrib import messages
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LoginView
from .models import CustomerUser
from .forms import CustomerUserCreateForm
from django.urls import reverse_lazy
from django.shortcuts import redirect

# def register(request):
#     if request.method == 'POST':
#         form = CustomerUserCreateForm(request.POST)
#         if form.is_valid():
#             form.save()
#     form = CustomerUserCreateForm()
#     return render(request, 'account/register.html', {'form': form})


class RegisterUserView(CreateView):
    model = CustomerUser
    template_name = 'account/register.html'
    form_class = CustomerUserCreateForm

    def get_success_url(self):
        return '/account/register/done'


class RegisterDoneView(TemplateView):
    template_name = 'account/register_done.html'


class LoginUserView(LoginView):
    template_name = 'account/login.html'
