from django import forms
from django.forms import ModelForm
from .models import Booking
from django.contrib.auth.models import User
import datetime as dt

class BookingForm(ModelForm):
    HOUR_CHOICES = [(dt.time(hour=x), '{:02d}:00'.format(x)) for x in range(8, 18)]
    audi_choices = [
        ('Auditorium','Auditorium'),
        ('Place2','Place2'),
        ('Place3','Place3')
    ]
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class' : 'form-control',
                'id' : 'validationTooltip01',
                'placeholder' : 'Name',
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'type': 'email',
                'class' : 'form-control',
                'id' : 'validationTooltip02',
                'placeholder' : 'Email',

            }
        )
    )
    date = forms.DateField(
        widget=forms.TextInput(
            attrs={
                'type': 'date',
                'class' : 'form-control',
                'id' : 'validationTooltip03',
                'placeholder' : 'Date',
            }
        )
    )
    place= forms.ChoiceField(
        choices = audi_choices,
        widget = forms.Select(
            attrs = {
                'class' : 'form-control',
                'id' : 'validationTooltip04',
                'placeholder' : 'Date',
            }
        )
    )
    start_time= forms.ChoiceField(
        choices = HOUR_CHOICES,
        widget = forms.Select(
            attrs = {
                'class' : 'form-control',
                'id' : 'validationTooltip04',
                'placeholder' : 'Date',
            }
        )
    )
    end_time= forms.ChoiceField(
        choices = HOUR_CHOICES,
        widget = forms.Select(
            attrs = {
                'class' : 'form-control',
                'id' : 'validationTooltip04',
                'placeholder' : 'Date',
            }
        )
    )
    class Meta:
        model = Booking
        fields = ('name','email','place','date','start_time','end_time')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(BookingForm, self).__init__(*args, **kwargs)
        self.fields['name'].initial = self.request.user.username
        self.fields['email'].initial = self.request.user.email