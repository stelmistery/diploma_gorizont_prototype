from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import CustomerUser
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from account.validators import validate_phone_number
from .models import Customer


class CustomerUserCreateForm(forms.ModelForm):
    # class Meta:
    #     fields = ('email', 'phone', 'password1', 'password2')
    #     model = CustomerUser
    #
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['phone'].label = 'Phone number'
    #     self.fields['email'].label = 'Email Address'

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

    def save(self, commit=True):
        customer = Customer.objects.create(phone=self.cleaned_data.get('phone'), email=self.cleaned_data.get('email'))

        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.customer_id = customer.id
        user.is_active = True
        if commit:
            user.save()


    class Meta:
        model = CustomerUser
        fields = ('phone', 'email', 'password1', 'password2')

