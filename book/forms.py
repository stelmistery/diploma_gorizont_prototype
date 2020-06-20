from django import forms
from .models import Category
from account.validators import validate_phone_number
from django.core.exceptions import ValidationError


class BookForm(forms.Form):
    number = (
        ("0", "0"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
    )
    check_in_date = forms.DateField(label='Дата заезда',
                                    widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    date_of_eviction = forms.DateField(label='Дата выезда',
                                       widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория',
                                      widget=forms.Select(attrs={'class': 'form-control'}))
    number_of_adults = forms.IntegerField(label='Количество взрослых',
                                          widget=forms.Select(attrs={'class': 'form-control'}, choices=number))
    number_of_children = forms.IntegerField(label='Количество детей',
                                            widget=forms.Select(choices=number, attrs={'class': 'form-control'}, ))

    def clean_number_of_adults(self):
        number_of_adults = self.cleaned_data.get('number_of_adults')
        if number_of_adults == 0:
            raise forms.ValidationError("Должен быть хотя бы один взрослый")
        return number_of_adults

    def clean(self):
        check_in_date = self.cleaned_data.get('check_in_date')
        date_of_eviction = self.cleaned_data.get('date_of_eviction')
        if check_in_date > date_of_eviction:
            errors = {'check_in_date': ValidationError(
                'Дата заезда не может быть позже даты выезда', code='invalid')}
            raise ValidationError(errors)


class DataForm(forms.Form):
    number = (
        ("0", "0"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
    )
    check_in_date = forms.DateField(label='Дата заезда',
                                    widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    date_of_eviction = forms.DateField(label='Дата выезда',
                                       widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория',
                                      widget=forms.Select(attrs={'class': 'form-control'}))
    number_of_adults = forms.IntegerField(label='Количество взрослых',
                                          widget=forms.Select(attrs={'class': 'form-control'}, choices=number))
    number_of_children = forms.IntegerField(label='Количество детей',
                                            widget=forms.Select(choices=number, attrs={'class': 'form-control'}, ))
    first_name = forms.CharField(label='Имя', max_length=50,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Фамилия', max_length=50,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    middle_name = forms.CharField(label='Отчество', max_length=50,
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label='Мобильный телефон', max_length=20, validators=[validate_phone_number],
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    additional_info = forms.CharField(label='Дополнительная информация', required=False,
                                      widget=forms.Textarea(attrs={'class': 'form-control'}))


class AuthDataForm(DataForm):
    first_name = forms.CharField(label='Имя', max_length=50,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True}))
    last_name = forms.CharField(label='Фамилия', max_length=50,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True}))
    middle_name = forms.CharField(label='Отчество', max_length=50,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True}))
    phone = forms.CharField(label='Мобильный телефон', max_length=20, validators=[validate_phone_number],
                            widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'readonly': True}))
