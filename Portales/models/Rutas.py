# importar de django models
from django.db import models


# crear el modelo
class Rutas(models.Model):
    nombre = models.CharField(max_length=150)
    zona_asignada = models.CharField(max_length=150)
    horario_inicio = models.DateTimeField(null=True)
    horario_fin = models.DateTimeField(null=True)
    buses = models.ForeignKey(
        'Buses', on_delete=models.CASCADE, related_name='rutas_asociadas', default=1)
    programas_Rutas = models.ForeignKey(
        'Programas_Rutas', on_delete=models.CASCADE, related_name='programas_rutas', default=1)

    def __str__(self):
        return self.nombre

# importar el modelo en el init para que pueda funcionar en las demás carpetas
