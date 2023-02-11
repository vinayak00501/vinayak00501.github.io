from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=60, default="")
    product_category = models.CharField(max_length=60, default="")
    product_sub_category = models.CharField(max_length=60, default="")
    price = models.IntegerField(default='-')
    desc = models.CharField(max_length=500, default="")
    image = models.ImageField(upload_to='app_ecom/images', default="")



    def __str__(self):
        return self.product_name
    


