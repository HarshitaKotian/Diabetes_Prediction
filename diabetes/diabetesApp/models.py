from django.db import models

# Create your models here.
class users(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=10)
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    email=models.CharField(max_length=25)
    address=models.CharField(max_length=100)

