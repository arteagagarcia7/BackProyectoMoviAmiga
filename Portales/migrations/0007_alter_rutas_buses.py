# Generated by Django 5.2.1 on 2025-06-11 01:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portales', '0006_alter_rutas_buses_alter_rutas_programas_rutas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rutas',
            name='buses',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='rutas_asociadas', to='Portales.buses'),
        ),
    ]
