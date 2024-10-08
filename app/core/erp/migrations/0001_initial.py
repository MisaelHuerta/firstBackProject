# Generated by Django 4.2.14 on 2024-08-06 01:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empoloyee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=150, verbose_name='Nombre Completo')),
                ('dni', models.CharField(max_length=10, unique=True, verbose_name='Identificacion')),
                ('date_joined', models.DateField(default=datetime.datetime(2024, 8, 5, 19, 35, 28, 253631), verbose_name='Fecha de registro')),
                ('date_creation', models.DateField(auto_now=True)),
                ('date_update', models.DateField(auto_now_add=True)),
                ('age', models.PositiveIntegerField(default=0)),
                ('salary', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('state', models.BooleanField(default=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatar/%Y/%m/%d')),
                ('cvitae', models.FileField(blank=True, null=True, upload_to='avatar/%Y/%m/%d')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
                'db_table': 'Empleado',
                'ordering': ['id'],
            },
        ),
    ]
