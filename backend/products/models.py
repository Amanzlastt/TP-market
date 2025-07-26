from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    
    """
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'


class Product(models.Model):
    PRODUCT_TYPES = [
        ("mobile",'Mobile Phone'),
        ('pc', 'pc'),
        ('tablet', 'Tablet',)
    ]

    name = models.CharField(max_length=200)
    type = models.CharField(max_length=50, choices=PRODUCT_TYPES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    specifications = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    