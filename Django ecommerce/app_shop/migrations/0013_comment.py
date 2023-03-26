# Generated by Django 4.1.3 on 2023-03-14 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_shop', '0012_remove_product_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created_on', models.DateField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_shop.product')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_shop.profile')),
            ],
        ),
    ]