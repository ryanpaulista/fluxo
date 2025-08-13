from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class User(AbstractUser):
    birth_date = models.DateField(
        null=True, 
        blank=True)
    phone_number = models.CharField(
        max_length=15, 
        null=True, 
        blank=True)

class Address(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='addresses')
    street = models.CharField(
        max_length=255, 
        null=False)
    city = models.CharField(
        max_length=100, 
        null=False)
    state = models.CharField(
        max_length=100, 
        null=False)
    zip_code = models.CharField(
        max_length=20, 
        null=False)
    country = models.CharField(
        max_length=100, 
        null=False)

