from django.db import models


class Tarjeta_Usuario(models.Model):
    saldo_actual = models.IntegerField(default=0)
    saldo_final = models.IntegerField(default=0)
