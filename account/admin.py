from django.contrib import admin
from .models import CustomerUser
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import Customer, PhoneOTP

admin.site.register(Customer)
admin.site.register(CustomerUser)
admin.site.register(PhoneOTP)