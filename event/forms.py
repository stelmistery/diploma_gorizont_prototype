from django import forms
from .models import Event, Member


class EventForms(forms.Form):
    name = forms.CharField(max_length=50, label='Наименование', widget=forms.TextInput(attrs={'class': 'form-control'}))
    type = forms.CharField(max_length=50, label='Тип мероприятия',
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label='Описание мероприятия',
                                  widget=forms.Textarea(attrs={'class': 'form-control', 'type': 'date'}))
    cost = forms.FloatField(label='Стоимость участия', widget=forms.TextInput(attrs={'class': 'form-control'}))
    start_date = forms.DateTimeField(label='Дата начала проведения',
                                     widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    end_date = forms.DateTimeField(label='Дата окончания проведения',
                                   widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    max_members = forms.IntegerField(label='Макс. кол-во участников',
                                     widget=forms.TextInput(attrs={'class': 'form-control'}))
    tech_support = forms.CharField(label='Техническое сопровождение',
                                   widget=forms.Textarea(attrs={'class': 'form-control'}))
    image = forms.ImageField(label='Главное изображение')

    def clean_image(self):
        image = self.cleaned_data['image']
        if image:
            return image