from django.db import models
from user.models import User
from catalog.models import Product

# Create your models here.

class Sale(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='sales')
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE, 
        related_name='sales')
    quantity = models.DecimalField(
        max_digits=10, 
        decimal_places=2)
    created_at = models.DateTimeField(
        auto_now_add=True)