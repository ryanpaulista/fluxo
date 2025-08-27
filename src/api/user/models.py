from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class User(AbstractUser):
    #first_name, last_name, email, password, is_active, is_superuser, last_login e data_joined 
    email = models.EmailField(
        unique=True, 
        null=False,)
    birth_date = models.DateField(
        null=True, 
        blank=True)
    phone_number = models.CharField(
        max_length=15, 
        null=True, 
        blank=True)
    password = models.CharField(
        max_length=128, 
        null=False, 
        blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username'] # afeta apenas o createsuperuser

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

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

