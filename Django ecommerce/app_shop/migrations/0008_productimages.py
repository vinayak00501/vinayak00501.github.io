# Generated by Django 4.1.3 on 2023-02-09 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_shop', '0007_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pr_id', models.IntegerField(default=0)),
                ('pr_image', models.ImageField(default='', upload_to='app_shop/images')),
                ('price', models.IntegerField(default=0)),
                ('color', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
