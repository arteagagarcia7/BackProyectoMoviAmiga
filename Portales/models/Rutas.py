# importar de django models
from django.db import models


# crear el modelo
class Rutas(models.Model):
    nombre = models.CharField(max_length=150)
    zona_asignada = models.CharField(max_length=150)
    horario_inicio = models.DateTimeField(null=True)
    horario_fin = models.DateTimeField(null=True)
    buses = models.ForeignKey('Buses', on_delete=models.PROTECT)
    programas_Rutas = models.ForeignKey(
        'Programas_Rutas', on_delete=models.PROTECT)

# importar el modelo en el init para que pueda funcionar en las demás carpetas
