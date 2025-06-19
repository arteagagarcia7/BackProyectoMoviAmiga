# Importamos pytest, que nos permite escribir pruebas simples y legibles

from django.core.exceptions import ValidationError
import pytest


# Importamos ValidationError para capturar errores de validación

# Este indica que la prueba usará la base de datos

@pytest.mark.django_db
def test_crear_bus_valido():
    # Importamos el modelo Buses dentro de la función para asegurar que Django esté inicializado
    from Portales.models.Buses import Buses

    # Antes de crear, eliminamos cualquier bus con el mismo código para evitar duplicados
    Buses.objects.filter(codigo_bus="ABC123").delete()

    # Creamos un objeto Bus con todos los campos válidos
    bus = Buses.objects.create(
        # cumple con el formato requerido (3 letras + 3 números)
        codigo_bus="ABC456",
        modelo="Mercedes-Benz",       # texto libre
        capacidad=150,                 # entero válido
        gps=True,                    # booleano
        tipo_transporte="Transmilenio"     # texto libre
    )

    # Verificamos que todos los datos se hayan guardado correctamente
    assert bus.codigo_bus == "ABC456"
    assert bus.modelo == "Mercedes-Benz"
    assert bus.capacidad == 150
    assert bus.gps is True
    assert bus.tipo_transporte == "Transmilenio"


# Otra prueba, también necesita acceso a la base de datos
@pytest.mark.django_db
def test_codigo_bus_invalido_lanza_error():
    # Importamos el modelo dentro de la función
    from Portales.models.Buses import Buses

    # Creamos un bus con código inválido (los números van primero)
    bus = Buses(
        # NO cumple el formato requerido (esperado: letras primero)
        codigo_bus="456DEF",
        modelo="Volvo",
        capacidad=150,
        gps=False,
        tipo_transporte="SITP"
    )

    # Esperamos que se genere un error de validación al verificar el formato
    # .full_clean() ejecuta todas las validaciones manualmente (como en un formulario)
    with pytest.raises(ValidationError):
        bus.full_clean()  # Esto lanza el error por el formato inválido del código_bus


# Otra prueba para validar que no se puedan duplicar los códigos de bus
@pytest.mark.django_db
def test_codigo_bus_duplicado_falla():
    # Importamos el modelo dentro de la función
    from Portales.models.Buses import Buses

    # Antes de crear, eliminamos cualquier bus con el código que vamos a usar
    Buses.objects.filter(codigo_bus="XYZ789").delete()

    # Creamos un primer bus con código válido
    Buses.objects.create(
        codigo_bus="DEF456",
        modelo="Volvo",
        capacidad=150,
        gps=True,
        tipo_transporte="SITP"
    )

    # Intentamos crear un segundo bus con el mismo código (que es único)
    # Esperamos que se genere una excepción por la restricción de unicidad
    # Aquí puede lanzarse IntegrityError u otra, según el backend de DB
    with pytest.raises(Exception):
        Buses.objects.create(
            codigo_bus="DEF456",          # código duplicado
            modelo="Scania",
            capacidad=260,
            gps=False,
            tipo_transporte="Transmilenio"
        )
