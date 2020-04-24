from django.db import models
from phone_field import PhoneField



class user(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    email = models.CharField(max_length=100)
    phone = PhoneField(blank=True, help_text='Contact phone number')
