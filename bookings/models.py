from django.db import models
from django.contrib.auth.models import User

class ArtClass(models.Model):
    # Tuples to control age and duration choices
    AGE_GROUP_CHOICES = (('5-7', '5-7 years old'), ('8-10', '8-10 years old'),)
    DURATION_CHOICES = (('1', '1 hour'), ('1.5', '1.5 hours'), ('2', '2 hours'),)

    title = models.CharField(max_length=100, unique=True, help_text='Enter a class title')
    description = models.CharField(max_length=200, help_text='Enter a brief class description', null=True, blank=True)
    start_date = models.DateField(help_text='Select the start date')
    end_date = models.DateField(help_text='Select the end date')
    duration = models.CharField(max_length=10,choices=DURATION_CHOICES, help_text='Enter the class duration')
    location = models.CharField(max_length=20, help_text='Enter class location')
    age_group = models.CharField(max_length=10,choices=AGE_GROUP_CHOICES)
    bookings_count = models.IntegerField(default=0)
    max_bookings = models.IntegerField(default=20)

    def __str__(self):
        return self.title



