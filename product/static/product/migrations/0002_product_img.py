# Generated by Django 3.1.3 on 2020-11-15 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(default='product_img/default_cake.png', upload_to='product_img/'),
        ),
    ]