from django.db import models
from django.contrib.auth.models import User


# Create your models here.
#this is our model class after then write migrate command and register




class School(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    contact = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name




class User(models.Model):
    name = models.CharField(max_length=70, unique=True)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    school = models.ForeignKey(School, on_delete=models.PROTECT, default=None)

    def __str__(self):
        return self.name
