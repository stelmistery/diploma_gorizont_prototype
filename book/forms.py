from django import forms
from .models import Book
from .models import Category
import datetime


class BookForm(forms.Form):
    number = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
    )

    check_in_date = forms.DateField(
        label='Дата заезда',
        widget=forms.DateInput(
            attrs={'class': 'form-control',
                   'type': 'date'}))

    date_of_eviction = forms.DateField(
        label='Дата выезда',
        widget=forms.DateInput(
            attrs={'class': 'form-control',
                   'type': 'date'}))

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label='Категория',
        widget=forms.Select(
            attrs={'class': 'form-control'}))

    number_of_adults = forms.IntegerField(
        label='Количество взрослых',
        widget=forms.Select(
            attrs={'class': 'form-control'},
            choices=number))

    number_of_children = forms.IntegerField(
        label='Количество детей',
        widget=forms.Select(
            choices=number,
            attrs={'class': 'form-control'},))


class DataForm(forms.Form):
    fio = forms.CharField(
        label='Фамилия имя отчество',
        max_length=50,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}))

    phone = forms.CharField(
        label='Мобильный телефон',
        max_length=10,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}))

    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs={'class': 'form-control'}))
