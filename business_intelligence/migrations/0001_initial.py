# Generated by Django 5.0.6 on 2024-06-06 02:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('licensePlate', models.CharField(max_length=50, unique=True)),
                ('brand', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('vin', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Mantenimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.CharField(max_length=50)),
                ('licensePlate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business_intelligence.vehicle')),
            ],
        ),
    ]
