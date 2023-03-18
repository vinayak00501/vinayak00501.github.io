# Generated by Django 4.1.3 on 2022-12-10 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default='', max_length=60)),
                ('product_category', models.CharField(default='', max_length=60)),
                ('product_sub_category', models.CharField(default='', max_length=60)),
                ('price', models.IntegerField(default='RS')),
                ('desc', models.CharField(default='', max_length=500)),
                ('image', models.ImageField(default='', upload_to='app_ecom/images')),
            ],
        ),
    ]