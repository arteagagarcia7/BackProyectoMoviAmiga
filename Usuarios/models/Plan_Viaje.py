from django.db import models


class Plan_Viaje(models.Model):
    punto_inicial = models.CharField(max_length=150)  # , null=True
    punto_final = models.CharField(max_length=150)
    rutas = models.ForeignKey('Portales.Rutas', on_delete=models.PROTECT)
    rutas_buses = models.ForeignKey('Portales.Buses', on_delete=models.PROTECT)
