from django.contrib import admin
from .models import Member, Event

# Register your models here.
admin.site.register(Event)
admin.site.register(Member)
