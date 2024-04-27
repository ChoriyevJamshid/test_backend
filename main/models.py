from django.db import models
from utils.models import BaseModel


class Product(BaseModel):

    title = models.CharField(max_length=255)
    code = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title


class Material(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class ProductMaterial(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='materials')
    material = models.ForeignKey(Material, on_delete=models.CASCADE,
                                 related_name='products')

    quantity = models.FloatField()

    def __str__(self):

        return f'{self.__class__.__name__}: {self.id}'


class Warehouse(BaseModel):
    material = models.ForeignKey(Material, on_delete=models.CASCADE,
                                 related_name='warehouses')
    remainder = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.__class__.__name__}: {self.id}"















