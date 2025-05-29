# importar de django models
from django.db import models


# crear el modelo
class Puntos_Recargas(models.Model):
    inclusion_discapacidad = models.BooleanField(default=False)
    inclusion_extranjeros = models.BooleanField(default=False)
    formas_pago = models.CharField(max_length=150)
    portales = models.ForeignKey('Portales', on_delete=models.PROTECT)

# importar el modelo en el init para que pueda funcionar en las demás carpetas
