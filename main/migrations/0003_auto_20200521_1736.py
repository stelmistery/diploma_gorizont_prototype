# Generated by Django 3.0.5 on 2020-05-21 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200521_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='Телефон'),
        ),
    ]
