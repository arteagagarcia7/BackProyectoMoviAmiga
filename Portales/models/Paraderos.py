# importar de django models
from django.db import models

# crear el modelo


class Paraderos(models.Model):
    inclusion_discapacidad = models.BooleanField(default=False)
    punto_asignado = models.CharField(max_length=150)
    capacidad_total_buses = models.IntegerField(default=0)

# importar el modelo en el init para que pueda funcionar en las demás carpetas
