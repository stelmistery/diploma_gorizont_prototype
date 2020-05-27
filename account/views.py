from django.shortcuts import render
from .forms import CustomerUserCreateForm
from django.contrib import messages
from django.views.generic import CreateView
from .models import CustomerUser
from .forms import CustomerUserCreateForm
from django.urls import reverse

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
    # success_url = reverse('register')
