from django.db import models
from django.contrib import admin
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager
# from django.contrib.auth import get_user_model
# User = get_user_model()
# Create your models here.

# Create your models here.
# class Userdetails(models.Model):
#     firstname=models.CharField(max_length=250)
#     lastname=models.CharField(max_length=250)
#     b_date=models.DateField
#     username=models.CharField(max_length=250)
#     password=   
    
    


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        
        return "{},{}".format(self.last_name, self.first_name)

   


# class Article(models.Model):
#     title = models.CharField(max_length=60)
#     date = models.DateTimeField()
#     author = models.ForeignKey(CustomUser)
#     vody = models.TextField()

    
    
        

    

