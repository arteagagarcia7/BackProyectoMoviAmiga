# Generated by Django 5.2.1 on 2025-06-11 02:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portales', '0007_alter_rutas_buses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buses',
            name='codigo_bus',
            field=models.CharField(max_length=6, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_codigo_bus', message='El código del bus debe tener el formato ABC123 (3 letras y 3 números en mayúscula).', regex='^[A-Z]{3}[0-9]{3}$')]),
        ),
    ]
