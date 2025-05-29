# importar de django models
from django.db import models


# crear el modelo
class Portales(models.Model):
    nombre = models.CharField(max_length=150)
    ubicacion = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre

# importar el modelo en el init para que pueda funcionar en las demás carpetas
