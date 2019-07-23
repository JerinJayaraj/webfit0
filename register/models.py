from django.db import models

# Create your models here.

class Register(models.Model):
    username= models.CharField(max_length=30)
    title = models.CharField(max_length=30)