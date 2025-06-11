from django.db import models
from django.core.validators import RegexValidator


class Buses(models.Model):
    # Cambiado de IntegerField a CharField con validador de formato tipo placa
    codigo_bus = models.CharField(
        max_length=6,
        validators=[
            # El egexValidator se asegura de que solo se permitan 3 letras
            # mayúsculas seguidas de 3 dígitos.
            RegexValidator(
                regex=r'^[A-Z]{3}[0-9]{3}$',
                message='El código del bus debe tener el formato ABC123 (3 '
                'letras y 3 números en mayúscula).',
                code='invalid_codigo_bus'
            )
        ],
        # Este evita que salgan tengan el mismo codigo_bus o sea la placa.
        unique=True
    )
    modelo = models.CharField(max_length=150)
    capacidad = models.IntegerField(default=0)
    gps = models.BooleanField(default=False)
    tipo_transporte = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.codigo_bus} - {self.modelo}'
