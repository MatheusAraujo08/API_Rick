# Generated by Django 4.2.4 on 2023-08-22 23:14

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meuApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('status', models.CharField(max_length=150)),
                ('species', models.CharField(max_length=150)),
                ('type', models.CharField(max_length=150)),
                ('gender', models.CharField(max_length=150)),
                ('created', models.DateTimeField(default=datetime.datetime(2023, 8, 22, 23, 14, 22, 909155, tzinfo=datetime.timezone.utc))),
            ],
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('air_date', models.DateTimeField(default=datetime.datetime(2023, 8, 22, 23, 14, 22, 909155, tzinfo=datetime.timezone.utc))),
                ('episode', models.CharField(max_length=150)),
                ('created', models.DateTimeField(default=datetime.datetime(2023, 8, 22, 23, 14, 22, 909155, tzinfo=datetime.timezone.utc))),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=150)),
                ('dimension', models.DecimalField(decimal_places=2, max_digits=10)),
                ('residents', models.BigIntegerField()),
                ('created', models.DateTimeField(default=datetime.datetime(2023, 8, 22, 23, 14, 22, 909155, tzinfo=datetime.timezone.utc))),
            ],
        ),
        migrations.DeleteModel(
            name='Personage',
        ),
        migrations.DeleteModel(
            name='Planet',
        ),
        migrations.AddField(
            model_name='character',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planet', to='meuApp.location'),
        ),
    ]
