from django import forms
from django.forms import ModelForm
from .models import Booking

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        widgets = {
            'date': forms.DateInput(attrs={'class':'datepicker'}),
        }
        fields = ('name','email','place','date','start_time','end_time')