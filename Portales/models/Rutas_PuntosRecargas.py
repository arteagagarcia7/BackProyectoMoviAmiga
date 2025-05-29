# importar de django models
from django.db import models


# crear el modelo
class Rutas_PuntosRecargas(models.Model):
    rutas = models.ForeignKey('Rutas', on_delete=models.PROTECT)
    buses = models.ForeignKey('Buses', on_delete=models.PROTECT)
    puntos_recargas = models.ForeignKey(
        'Puntos_Recargas', on_delete=models.PROTECT)

# importar el modelo en el init para que pueda funcionar en las demás carpetas
