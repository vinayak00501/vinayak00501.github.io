from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

User = get_user_model()


class Profile(models.Model):

    profile_id = models.IntegerField(default=-1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_img = models.ImageField(upload_to="app_shop/profile_images", default="/media/app_shop/profile_images/default_img.png")
    location = models.CharField(max_length=200, default="")

    def __str__(self):
        return  self.user.username

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=150, default="")
    product_price = models.IntegerField(default=0)
    product_desc = models.CharField(max_length=600, default="")
    primary_img = models.ImageField(upload_to="app_shop/images", default="")
    category1 = models.CharField(max_length=90, default="product")
    category2 = models.CharField(max_length=90, default="product")
    category3 = models.CharField(max_length=90, default="product")
    images = models.CharField(max_length=1000, default="")
    img_id = models.IntegerField(default=-1)

    

    
    def __str__(self):
        return self.product_name
    
class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user_profile.user.username



class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_item = models.JSONField()


class ProductImage(models.Model):
    image_id = models.AutoField(primary_key=True)
    image_of = models.ForeignKey(Product, default="",on_delete=models.CASCADE)
    image = models.ImageField(upload_to="app_shop/images")
    price = models.IntegerField(default=0)
    color = models.CharField(max_length=50, default="")

