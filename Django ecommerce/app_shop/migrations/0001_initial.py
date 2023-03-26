# Generated by Django 4.1.3 on 2023-01-22 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(default='', max_length=150)),
                ('product_price', models.IntegerField(default=0)),
                ('product_desc', models.CharField(default='', max_length=600)),
                ('images', models.FileField(upload_to='app_shop/images')),
            ],
        ),
    ]