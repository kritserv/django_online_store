# Generated by Django 4.2.5 on 2023-09-18 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='model_img/brands/'),
        ),
        migrations.AddField(
            model_name='computer',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='model_img/computers/'),
        ),
    ]
