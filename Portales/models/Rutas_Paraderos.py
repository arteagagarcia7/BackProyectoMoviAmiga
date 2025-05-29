# importar de django models
from django.db import models


# crear el modelo
class Rutas_Paraderos(models.Model):
    rutas = models.ForeignKey('Rutas', on_delete=models.PROTECT)
    buses = models.ForeignKey('Buses', on_delete=models.PROTECT)
    paraderos = models.ForeignKey('Paraderos', on_delete=models.PROTECT)

# importar el modelo en el init para que pueda funcionar en las demás carpetas
