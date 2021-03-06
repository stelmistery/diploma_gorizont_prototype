# Generated by Django 3.0.5 on 2020-06-08 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование')),
                ('type', models.CharField(max_length=50, verbose_name='Тип мероприятия')),
                ('description', models.TextField(verbose_name='Описание мероприятия')),
                ('cost', models.FloatField(blank=True, default=0, null=True, verbose_name='Стоимость участия')),
                ('start_date', models.DateTimeField(verbose_name='Дата начала проведения')),
                ('end_date', models.DateTimeField(verbose_name='Дата окончания проведения')),
                ('max_members', models.IntegerField(blank=True, null=True, verbose_name='Макс. кол-во участников')),
                ('tech_support', models.TextField(blank=True, null=True, verbose_name='Техническое сопровождение')),
                ('status', models.BooleanField(default=0, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятия',
                'ordering': ['start_date'],
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderer', models.BooleanField(default=0, verbose_name='Заказчик')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Customer', verbose_name='Клиент')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Event', verbose_name='Мероприятие')),
            ],
            options={
                'verbose_name': 'Участник',
                'verbose_name_plural': 'Участники',
            },
        ),
    ]
