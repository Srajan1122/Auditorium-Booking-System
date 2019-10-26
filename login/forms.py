from django import forms
from django.forms import ModelForm
from .models import Booking

class BookingForm(ModelForm):
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
    start_time= forms.TimeField(
        widget=forms.TextInput(
            attrs={
                'type': 'time',
                'class' : 'form-control',
                'id' : 'validationTooltip05',
            }
        )
    )
    end_time= forms.TimeField(
        widget=forms.TextInput(
            attrs={
                'type': 'time',
                'class' : 'form-control',
                'id' : 'validationTooltip06',
            }
        )
    )
    class Meta:
        model = Booking
        fields = ('name','email','place','date','start_time','end_time')