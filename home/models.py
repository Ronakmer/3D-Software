from unicodedata import name
from django.db import models
# from passlib.hash import pbkdf2_sha256
# Create your models here.

class signup(models.Model):
    name = models.CharField(max_length=30)
    # last_name = models.CharField(max_length=30)
    phone_number  = models.CharField(max_length=30)
    gmail= models.CharField(max_length=30)
    address= models.CharField(max_length=30)
    # city= models.CharField(max_length=30)
    # password= models.TextField(max_length=300)
    # password2=models.e
    

    def __str__(self):
        return f"{self.first_name}"

class user(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user_name = models.CharField(max_length=30)
    gmail= models.CharField(max_length=30)
    address= models.CharField(max_length=30)
    city= models.CharField(max_length=30)
    password= models.CharField(max_length=300)
    # password2=models.e
    

    def __str__(self):
        return f"{self.first_name}"