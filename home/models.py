from unicodedata import name
from django.db import models
# from passlib.hash import pbkdf2_sha256
# Create your models here.

class signup(models.Model):
    username = models.CharField(max_length=30,default="")
    # last_name = models.CharField(max_length=30)
    # phone_number  = models.ImageField(max_length=30)
    # gmail= models.CharField(max_length=30)
    # address= models.CharField(max_length=30)
    # city= models.CharField(max_length=30)
    password= models.CharField(max_length=30,default="")
    # password2=models.e
    

    def __str__(self):
        return f"{self.username}"

class user(models.Model):
    name = models.CharField(max_length=30,default="")
    username = models.CharField(max_length=30,default="")
    phone_number  = models.IntegerField(default=0)
    gmail= models.CharField(max_length=30,default="")
    address= models.CharField(max_length=30,default="")
    # city= models.CharField(max_length=30)
    password= models.CharField(max_length=30,default="")
    # password2=models.e
    

    def __str__(self):
        return f"{self.name}"