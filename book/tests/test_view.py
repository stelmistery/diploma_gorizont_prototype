from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from book.models import Category, Room, Book
import json
import datetime
from book.forms import BookForm, DataForm, AuthDataForm

#
# class TestForms(SimpleTestCase):
#     def test_book_form_valid_data(self):
#         form = BookForm(data={
#             'check_in_date': datetime.datetime('2020'),
#             'date_of_eviction': '2020/12/08',
#             # 'check_in_date': '2020/12/07',
#             # 'date_of_eviction': '2020/12/08',
#             'category': 2,
#             'number_of_adults': 2,
#             'number_of_children': 1
#         })
#
#         self.assertTrue(form.is_valid())
#
#     def test_expense_form_no_data(self):
#         form = BookForm(data={})
#
#         self.assertFalse(form.is_valid())
#         self.assertEqual(len(form.errors), 5)


        #
        # number_of_children = forms.IntegerField(label='Количество детей',
        #                                         widget=forms.Select(choices=number, attrs={'class': 'form-control'}, ))
        # first_name = forms.CharField(label='Имя', max_length=50,
        #                              widget=forms.TextInput(attrs={'class': 'form-control'}))
        # last_name = forms.CharField(label='Фамилия', max_length=50,
        #                             widget=forms.TextInput(attrs={'class': 'form-control'}))
        # middle_name = forms.CharField(label='Отчество', max_length=50,
        #                               widget=forms.TextInput(attrs={'class': 'form-control'}))
        # phone = forms.CharField(label='Мобильный телефон', max_length=20, validators=[validate_phone_number],
        #                         widget=forms.TextInput(attrs={'class': 'form-control'}))
        # email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
        # additional_info = forms.CharField(label='Дополнительная информация', required=False,
        #                                   widget=forms.Textarea(attrs={'class': 'form-control'}))
        #
        # def test_book_form_valid_data(self):
        #     form = BookForm(data={
        #         'check_in_date': datetime.datetime(2020, 7, 14),
        #         'date_of_eviction': datetime.datetime(2020, 7, 14),
        #         'category': 2,
        #         'number_of_adults': 2,
        #         'first_name': 'Vladislav',
        #         'last_name': 'Voznesenskiy',
        #         'middle_name': 'Aleksandrovich',
        #         'phone': '+79787370176',
        #         'email': 'adminnn@mail.ru'
        #     })