from django.db import models
from django.contrib.auth.models import User
import datetime as dt

# Create your models here.
class Booking(models.Model):
    HOUR_CHOICES = [(dt.time(hour=x), '{:02d}:00'.format(x)) for x in range(8, 18)]
    audi_choices = [
        ('Auditorium','Auditorium'),
        ('Place2','Place2'),
        ('Place3','Place3')
    ]
    default_choice = [
        ('Auditorium','Auditorium')
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField()
    place = models.CharField(max_length=100, choices = audi_choices,default=default_choice)
    date = models.DateField()
    start_time = models.TimeField(choices= HOUR_CHOICES)
    end_time = models.TimeField(choices= HOUR_CHOICES)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name