from django.db import models
from core.models import BaseModel, User 

class Category (BaseModel):
    category_id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=100)
    cat = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.type


class Attribute(BaseModel):
    attribute_id = models.IntegerField(primary_key=True)
    color = models.IntegerField(null=True)
    size = models.CharField(max_length=20, blank=False, null=False)
    stock = models.IntegerField()
    price = models.FloatField()
    short_description = models.CharField(max_length=512, blank=True, null=True)


class Product(BaseModel):
    product_id = models.IntegerField(primary_key=True)
    type = models.IntegerField()   #type of the model 
    categories = models.ForeignKey(Category, on_delete=models.RESTRICT)
    attribute = models.OneToOneField(Attribute, on_delete=models.RESTRICT)

    def __str__(self):
        return str(self.product_id)

class Image(BaseModel):
    image_id = models.IntegerField(primary_key=True)
    image = models.BinaryField(blank=False, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Discount(BaseModel):
    discount_id = models.IntegerField(primary_key=True)
    percent = models.IntegerField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)

class Order(BaseModel):
    order_id = models.IntegerField(primary_key=True)
    total_amount = models.FloatField(blank=False, null=False)
    created_at = models.DateField(auto_now=True, blank=False, null=False)
    products = models.ManyToManyField(Product)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    discount = models.OneToOneField(Discount, on_delete=models.RESTRICT, blank=True, null=True)

    def __str__(self):
        return str(self.order_id)


class Address(BaseModel):
    address_id = models.IntegerField(primary_key=True)
    postal_code = models.BigIntegerField(blank=False, null=False)
    address = models.TextField(blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)