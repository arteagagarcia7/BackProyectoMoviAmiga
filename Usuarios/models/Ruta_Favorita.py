from django.db import models


class Ruta_Favorita(models.Model):
    nombre = models.CharField(max_length=150)
    Punto_Inicial = models.CharField(max_length=150)
    Punto_Final = models.CharField(max_length=150)
