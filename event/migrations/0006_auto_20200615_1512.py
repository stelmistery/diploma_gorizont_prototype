# Generated by Django 3.0.5 on 2020-06-15 15:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_event_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 15, 15, 12, 18, 862384)),
        ),
        migrations.AddField(
            model_name='event',
            name='pub_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
