from django.db import models


class Recarga(models.Model):
    monto = models.IntegerField(default=0)
    fecha = models.DateTimeField(null=True)
    medio = models.CharField(max_length=150)
