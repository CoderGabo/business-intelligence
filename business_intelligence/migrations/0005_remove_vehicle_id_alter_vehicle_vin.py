# Generated by Django 5.0.6 on 2024-06-07 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_intelligence', '0004_rename_vin_mantenimiento_vehicle_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='id',
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vin',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
