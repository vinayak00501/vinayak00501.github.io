from django.contrib import admin
from .models import Product, Order, Profile, Comment, ProductImage

# Register your models here.
admin.site.register([Product, Order, Profile, Comment, ProductImage])

