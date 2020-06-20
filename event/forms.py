from django import forms
from .models import Event, Member
from django.core.exceptions import ValidationError


class EventForms(forms.Form):
    name = forms.CharField(max_length=50, label='Наименование', widget=forms.TextInput(attrs={'class': 'form-control'}))
    type = forms.CharField(max_length=50, label='Тип мероприятия',
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label='Описание мероприятия',
                                  widget=forms.Textarea(attrs={'class': 'form-control', 'type': 'date'}))
    cost = forms.FloatField(label='Стоимость участия', required=False,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    start_date = forms.DateTimeField(label='Дата начала проведения',
                                     widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    end_date = forms.DateTimeField(label='Дата окончания проведения',
                                   widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    max_members = forms.IntegerField(label='Макс. кол-во участников', required=False,
                                     widget=forms.TextInput(attrs={'class': 'form-control'}))
    tech_support = forms.CharField(label='Техническое сопровождение', required=False,
                                   widget=forms.Textarea(attrs={'class': 'form-control'}))
    image = forms.ImageField(label='Главное изображение')

    def clean_cost(self):
        cost = self.cleaned_data.get('cost')
        if cost == '':
            cost = int(cost)
        return cost

    def clean(self):
        start_date = self.cleaned_data.get('start_date')
        end_date = self.cleaned_data.get('end_date')
        if start_date > end_date:
            errors = {'check_in_date': ValidationError(
                'Дата начала не может быть позже даты окончания', code='invalid')}
            raise ValidationError(errors)