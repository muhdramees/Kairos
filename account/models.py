from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
import random



# Create your models here.

class EmailUser(AbstractUser, BaseUserManager):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    username = models.CharField(max_length=255, null=True)
    password = models.CharField(max_length=100)
    re_type_password = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    # token = models.CharField(max_length=100, default=None)
    # is_blocked = models.BooleanField(default=False)
    # is_blocked = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=13, null=True)
    # otp = models.IntegerField(null=False, default=00000)
    # created_at = models.DateTimeField(auto_now_add=True)
    blocked=models.BooleanField(default=False)




class Otp(models.Model):
    phone_number = models.CharField(max_length=13)
    otp = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)