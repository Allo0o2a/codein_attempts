from django.db import models

from django.contrib.auth.models import UserManager, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser
# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=12)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    LANGUAGE_CHOICES = ((1, 'Regular User'), (2, 'Python'), (3, 'Java'), (4, 'C'), (5, 'C++'), (6, 'Ruby'), (7, 'Go'), (8, 'Web Developer'), (9, 'Other Language'))
    developer = models.IntegerField(choices=LANGUAGE_CHOICES, default='1')
##    developer = models.BooleanField(default=False)
##    python = models.BooleanField(default=False)
##    java = models.BooleanField(default=False)
##    standard_c = models.BooleanField(default=False)
##    c_plus_plus = models.BooleanField(default=False)
##    other_language = models.CharField(max_length=12)
    
class Portfolio(models.Model):
    user = models.ForeignKey('server.User', on_delete=models.CASCADE)
    port_image = models.ImageField(upload_to="")
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__ (self):
        return self.user.username



class Project(models.Model):
    user = models.ForeignKey('server.User', on_delete=models.CASCADE)
    proj_name = models.CharField(max_length=255, null=True)
    proj_description = models.TextField()
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__ (self):
        return self.user.username
