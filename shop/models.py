from django.db import models
from core.models import BaseModel, User


class Products(BaseModel):
    product_id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=100, blank=False, null=False)

class Attribute(BaseModel):
    attribute_id = models.IntegerField(primary_key=True)
    color = models.CharField(max_length=100, blank=True, null=True)
    size = models.CharField(max_length=100, blank=False, null=False)
    stock = models.IntegerField()
    price = models.FloatField()
    products = models.ManyToManyField(Products)


class Orders(BaseModel):
    order_id = models.IntegerField(primary_key=True)
    total_amount = models.FloatField(blank=False, null=False)
    date = models.DateField(auto_now=True, blank=False, null=False)
    products = models.ManyToManyField(Products)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Discount(BaseModel):
    discount_id = models.IntegerField(primary_key=True)
    percent = models.IntegerField(blank=True)
    amount = models.FloatField(blank=True)
    orders = models.OneToOneField(Orders, on_delete=models.CASCADE)

class Address(BaseModel):
    address_id = models.IntegerField(primary_key=True)
    postal_code = models.BigIntegerField(blank=False, null=False)
    address = models.TextField(blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)