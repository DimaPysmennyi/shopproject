from django.db import models

# Create your models here.
class UserForm(models.Model):
    login = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    email = models.CharField(max_length=100)
    phone_number = models.IntegerField()