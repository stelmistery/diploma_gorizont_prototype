from django import forms
from .models import CustomerUser
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from account.validators import validate_phone_number
from .models import Customer


class CustomerUserCreateForm(forms.ModelForm):
    first_name = forms.CharField(label='Имя', max_length=50,
                                 widget=forms.TextInput())
    last_name = forms.CharField(label='Фамилия', max_length=50,
                                widget=forms.TextInput())
    middle_name = forms.CharField(label='Отчество', max_length=50,
                                  widget=forms.TextInput())
    phone = forms.CharField(required=True, label='Мобильный телефон', validators=[validate_phone_number], max_length=20)
    email = forms.EmailField(required=True, label='Адрес электронной почты')
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput,
                                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput,
                                help_text='Введите пароль повторно для проверки')

    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        if password1:
            password_validation.validate_password(password1)
        return password1

    def clean(self):
        super().clean()
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            errors = {'password2': ValidationError(
                'Ввдённые пароли не совпадают', code='password_mismatch')}
            raise ValidationError(errors)


    class Meta:
        model = CustomerUser
        fields = ('first_name', 'last_name', 'middle_name', 'phone', 'email', 'password1', 'password2')


class PhoneVerify(forms.Form):
    phone = forms.CharField(required=True, label='Мобильный телефон', validators=[validate_phone_number], max_length=20,
                            widget=forms.HiddenInput)
    code = forms.CharField(required=True, label='Код из СМС', max_length=4)
