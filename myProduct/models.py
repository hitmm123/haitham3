from django.db import models

# Create your models here.
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('Food', 'Food'),
        ('Snacks', 'Snacks'),
        ('Drinks', 'Drinks'),
        ('Hardware', 'Hardware'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.name
