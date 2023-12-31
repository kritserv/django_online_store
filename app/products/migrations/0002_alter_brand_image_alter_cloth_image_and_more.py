# Generated by Django 4.2.5 on 2023-09-21 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/model_img/brands/'),
        ),
        migrations.AlterField(
            model_name='cloth',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/model_img/cloths/'),
        ),
        migrations.AlterField(
            model_name='computer',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/model_img/computers/'),
        ),
        migrations.AlterField(
            model_name='headphone',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/model_img/headphones/'),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/model_img/smartphones/'),
        ),
    ]
