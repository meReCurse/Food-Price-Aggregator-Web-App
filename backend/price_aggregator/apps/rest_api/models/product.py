from django.db import models
from rest_framework import serializers

from .shop import Shop

# Create your models here.
__all__ = ('Product', 'ProductSerializer')


class ProductBase(models.Model):
    class Meta:
        abstract = True


class Product(ProductBase):
    class Meta:
        ordering = ['date']

    shop = models.ForeignKey(
        Shop,
        verbose_name='Shop',
        on_delete=models.CASCADE
    )
    name = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    date = models.DateField(auto_now=True)


class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        abstract = True


class ProductSerializer(BaseSerializer):
    class Meta:
        model = Product
        fields = ['id', 'shop', 'name', 'price', 'date']

