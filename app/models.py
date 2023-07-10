from _decimal import Decimal

from django.db import models
from django.utils.text import slugify

# Create your models here.

class Product(models.Model):
    nominal = models.CharField(max_length=255)
    variasi = models.CharField(max_length=255)
    koin_smile_one = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))


class ratebrl(models.Model):
    rate = models.DecimalField(max_digits=20, decimal_places=6, default=Decimal('0.00'))
    date_rate = models.TimeField
