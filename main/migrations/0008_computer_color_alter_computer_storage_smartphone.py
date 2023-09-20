# Generated by Django 4.2.5 on 2023-09-19 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_computer_is_laptop'),
    ]

    operations = [
        migrations.AddField(
            model_name='computer',
            name='color',
            field=models.CharField(default='Black', max_length=100),
        ),
        migrations.AlterField(
            model_name='computer',
            name='storage',
            field=models.CharField(choices=[('128Gb', '128Gb'), ('256Gb', '256Gb'), ('512Gb', '512Gb'), ('1Tb', '1Tb'), ('2Tb', '2Tb'), ('4Tb', '4Tb')], default='512Gb', max_length=10),
        ),
        migrations.CreateModel(
            name='Smartphone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='model_img/smartphones/')),
                ('color', models.CharField(default='White', max_length=100)),
                ('is_instock', models.BooleanField(default=True)),
                ('instocks', models.IntegerField(default=100)),
                ('is_onsale', models.BooleanField(default=True)),
                ('og_price', models.IntegerField(default=22000)),
                ('price', models.IntegerField(default=19900)),
                ('stars', models.FloatField(default=5.0)),
                ('is_recommend', models.BooleanField(default=False)),
                ('is_tablet', models.BooleanField(default=False)),
                ('is_flagship', models.BooleanField(default=False)),
                ('processor', models.CharField(max_length=100)),
                ('processor_brand', models.CharField(choices=[('Snapd', 'Snapd'), ('Easy', 'Easy')], default='Snapd', max_length=10)),
                ('ram', models.CharField(choices=[('3Gb', '3Gb'), ('4Gb', '4Gb'), ('8Gb', '8Gb'), ('6Gb', '6Gb'), ('12Gb', '12Gb'), ('16Gb', '16Gb')], default='6Gb', max_length=10)),
                ('storage', models.CharField(choices=[('32Gb', '32Gb'), ('64Gb', '64Gb'), ('128Gb', '128Gb'), ('256Gb', '256Gb'), ('512Gb', '512Gb')], default='128Gb', max_length=10)),
                ('size', models.CharField(blank=True, choices=[('5.8"', '5.8"'), ('6.0"', '6.0"'), ('6.2"', '6.2"'), ('6.4"', '6.4"'), ('6.6"', '6.6"'), ('6.8"', '6.8"'), ('9.7"', '9.7"'), ('10.1"', '10.1"'), ('12"', '12"')], default='6.2"', max_length=10)),
                ('resolution', models.CharField(blank=True, choices=[('1080P', '1080P'), ('1440P', '1440P'), ('4K', '4K')], default='1440P', max_length=10)),
                ('refreshrate', models.CharField(blank=True, choices=[('60Hz', '60Hz'), ('75Hz', '75Hz'), ('90Hz', '90Hz'), ('120Hz', '120Hz'), ('144Hz', '144Hz'), ('240Hz', '240Hz')], default='90Hz', max_length=10)),
                ('display', models.CharField(blank=True, choices=[('Ips', 'Ips'), ('Va', 'Va'), ('Oled', 'Oled')], default='Ips', max_length=10)),
                ('weight', models.FloatField(default=0.14)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.brand')),
            ],
        ),
    ]