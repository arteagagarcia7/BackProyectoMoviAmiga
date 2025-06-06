from django.db import models


class Ruta_Favorita(models.Model):
    nombre = models.CharField(max_length=150)
