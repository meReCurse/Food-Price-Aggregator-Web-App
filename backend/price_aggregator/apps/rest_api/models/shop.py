from django.db import models
from rest_framework import serializers

# Create your models here.
__all__ = ('Shop', 'ShopSerializer')


class ShopBase(models.Model):
    class Meta:
        abstract = True


class Shop(ShopBase):
    class Meta:
        ordering = ['name']

    name = models.TextField()
    url = models.URLField()


class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        abstract = True


class ShopSerializer(BaseSerializer):
    class Meta:
        model = Shop
        fields = ['id', 'name', 'url']
