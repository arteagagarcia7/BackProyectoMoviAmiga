# importar de django models
from django.db import models


# crear el modelo
class Programas_Rutas(models.Model):
    recorrido_actualizado = models.CharField(max_length=150)
    tiempo_actualizado = models.CharField(max_length=150)
    vias_acceso = models.CharField(max_length=150)
    # Null=true vacio por si no requiere datos
    horario_inicio = models.DateTimeField(null=True)
    horario_fin = models.DateTimeField(null=True)
    afluencia_personas = models.IntegerField(default=0)
    # portal_origen = models.ForeignKey('Portales', on_delete=models.PROTECT,
    #  related_name='punto_origen') se documenta porque no mostraba datos
    # portal_final = models.ForeignKey('Portales', on_delete=models.PROTECT,
    #  related_name='punto_final') se documenta porque no mostraba datos
    portal_origen = models.ForeignKey(
        'Portales', on_delete=models.CASCADE, related_name='rutas_como_origen', default=1)
    portal_final = models.ForeignKey(
        'Portales', on_delete=models.CASCADE, related_name='rutas_como_destino', default=1)

    # se usa def para que liste un atributo especifico

    def __str__(self):
        return f'{self.portal_origen.nombre} a {self.portal_final.nombre}'
# importar el modelo en el init para que pueda funcionar en las demás carpetas
# se pone en las llaves foraneas cascede.
