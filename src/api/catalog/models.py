from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(
        max_length=255, 
        null=False)
    description = models.TextField(
        null=True, 
        blank=True)
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        null=False)
    stock = models.PositiveIntegerField(
        default=0)
