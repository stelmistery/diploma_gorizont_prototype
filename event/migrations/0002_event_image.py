# Generated by Django 3.0.5 on 2020-06-14 15:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='image/'),
            preserve_default=False,
        ),
    ]
