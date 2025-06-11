from django.db import models


class Tarjeta_Usuario(models.Model):
    saldo_actual = models.IntegerField(default=0)
    numero_tarjeta = models.IntegerField(default=0)
