from django.shortcuts import render
from urllib.request import urlopen
from urllib.error import URLError
from urllib.parse import quote
from django.http.response import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'main/index.html')
