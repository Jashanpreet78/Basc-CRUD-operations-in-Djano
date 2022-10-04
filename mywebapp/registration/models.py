from django.db import models
from datetime import datetime,date
from django import forms

# Create your models here.
class User(models.Model):
    task_name= models.CharField(max_length=60)
    description=models.CharField(max_length=100)
    created_date=models.DateTimeField(auto_now_add=False)
    finished_date=models.DateTimeField(auto_now_add=False)
    status=models.CharField(max_length=50)
