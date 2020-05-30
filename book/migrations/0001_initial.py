# Generated by Django 3.0.5 on 2020-05-30 09:35

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('conditions', models.TextField(verbose_name='Условия')),
                ('price', models.IntegerField(verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['price'],
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_number', models.CharField(max_length=5, primary_key=True, serialize=False, verbose_name='Номер комнаты')),
                ('number_of_place', models.IntegerField(verbose_name='Кол-во мест')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Category', verbose_name='Номер категории')),
            ],
            options={
                'verbose_name': 'Комната',
                'verbose_name_plural': 'Команты',
                'ordering': ['room_number'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('Book_code', models.AutoField(primary_key=True, serialize=False, verbose_name='Код брони')),
                ('number_of_adults', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(4)], verbose_name='Кол-во взрослых')),
                ('number_of_children', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(4)], verbose_name='Кол-во детей')),
                ('check_in_date', models.DateField(verbose_name='Дата заселения')),
                ('date_of_eviction', models.DateField(verbose_name='Дата выселения')),
                ('additional_information', models.TextField(blank=True, null=True, verbose_name='Дополнительная информация')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Сумма')),
                ('confirmed', models.BooleanField(default=False, verbose_name='Подтвержедено')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Customer', verbose_name='Клиент')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Room', verbose_name='Номер комнаты')),
            ],
            options={
                'verbose_name': 'Бронь',
                'verbose_name_plural': 'Брони',
            },
        ),
    ]
