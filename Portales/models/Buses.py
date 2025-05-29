# importar de django models
from django.db import models

# crear el modelo


class Buses(models.Model):
    codigo_bus = models.IntegerField(default=0)
    modelo = models.CharField(max_length=150)
    capacidad = models.IntegerField(default=0)
    gps = models.BooleanField(default=False)

    def __str__(self):
        return self.modelo

# importar el modelo en el init para que pueda funcionar en las demás carpetas
