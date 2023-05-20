from django.contrib import admin
from shop.models import Category, Attribute, Product, Image, Discount, Order, Address

admin.site.register([Category, Attribute, Product, Image, Discount, Order, Address])