# Generated by Django 5.0.6 on 2024-06-06 22:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_intelligence', '0002_alter_mantenimiento_table_alter_vehicle_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'service',
            },
        ),
        migrations.RenameField(
            model_name='mantenimiento',
            old_name='licensePlate',
            new_name='vin',
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='licensePlate',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vin',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterModelTable(
            name='mantenimiento',
            table='maintenance',
        ),
        migrations.CreateModel(
            name='ServicioMantenimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maintenance_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business_intelligence.mantenimiento')),
                ('service_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business_intelligence.servicio')),
            ],
            options={
                'db_table': 'service_maintenance',
            },
        ),
    ]
