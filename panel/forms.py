from django import forms
from book.models import Category
from account.validators import validate_phone_number


class PanelBookForm(forms.Form):
    number = (
        ("0", "0"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
    )
    check_in_date = forms.DateField(label='Дата заезда',
                                    widget=forms.DateInput(
                                        attrs={'class': 'form-control text-center',
                                               'type': 'text',
                                               'placeholder': 'От',
                                               'id': 'example-daterange1'}))

    date_of_eviction = forms.DateField(label='Дата выезда',
                                       widget=forms.DateInput(
                                           attrs={'class': 'form-control text-center',
                                                  'type': 'text',
                                                  'placeholder': 'До',
                                                  'id': 'example-daterange2'}))

    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория',
                                      widget=forms.Select(
                                          attrs={'class': 'form-control',
                                                 'size': '1',
                                                 'id': 'example-select'}))

    number_of_adults = forms.IntegerField(label='Количество взрослых',
                                          widget=forms.Select(
                                              choices=number,
                                              attrs={'class': 'form-control',
                                                     'size': '1',
                                                     'id': 'example-select'}))

    number_of_children = forms.IntegerField(label='Количество детей',
                                            widget=forms.Select(
                                                choices=number,
                                                attrs={'class': 'form-control',
                                                       'size': '1',
                                                       'id': 'example-select'}))


class PanelDataForm(forms.Form):
    number = (
        ("0", "0"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
    )
    check_in = forms.DateField(label='Дата заезда',
                               widget=forms.DateInput(
                                   attrs={'class': 'form-control text-center',
                                          'type': 'text',
                                          'id': 'example-daterange1',
                                          'placeholder': 'От'}))

    departure = forms.DateField(label='Дата выезда',
                                widget=forms.DateInput(
                                    attrs={'class': 'form-control text-center',
                                           'type': 'text',
                                           'id': 'example-daterange2',
                                           'placeholder': 'По'}))

    category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                      label='Категория',
                                      widget=forms.Select(attrs={'class': 'form-control'}))

    number_of_adults = forms.IntegerField(label='Количество взрослых',
                                          widget=forms.Select(
                                              attrs={'class': 'form-control'},
                                              choices=number))

    number_of_children = forms.IntegerField(label='Количество детей',
                                            widget=forms.Select(
                                                choices=number,
                                                attrs={'class': 'form-control',
                                                       'id': 'number_of_children'}, ))

    first_name = forms.CharField(label='Имя',
                                 max_length=50,
                                 widget=forms.TextInput(
                                     attrs={'class': 'form-control',
                                            'id': 'first_name',
                                            'placeholder': 'Имя'}))

    last_name = forms.CharField(label='Фамилия',
                                max_length=50,
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control',
                                           'id': 'last_name',
                                           'placeholder': 'Фамилия'}))

    middle_name = forms.CharField(label='Отчество',
                                  max_length=50,
                                  widget=forms.TextInput(
                                      attrs={'class': 'form-control',
                                             'id': 'middle_name',
                                             'placeholder': 'Отчество'}))

    phone = forms.CharField(label='Мобильный телефон',
                            max_length=20, validators=[validate_phone_number],
                            widget=forms.TextInput(
                                attrs={'class': 'form-control',
                                       'id': 'masked_phone',
                                       'placeholder': '+7(999) 999-9999'}))

    email = forms.EmailField(label='Email',
                             widget=forms.EmailInput(
                                 attrs={'class': 'form-control',
                                        'id': 'email',
                                        'placeholder': 'email'}))

    additional_info = forms.CharField(label='Дополнительная информация',
                                      required=False,
                                      widget=forms.Textarea(
                                          attrs={'class': 'form-control',
                                                 'id': 'additional_info'}))
