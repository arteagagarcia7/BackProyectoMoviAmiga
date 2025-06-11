from rest_framework import viewsets

# importo el modelo creado que corresponde
from Portales.models import Programas_Rutas

# importo el serializador creado que corresponde
from Portales.serializers import Programas_RutasSerializers


# crear la vista
class Programas_RutasViewset(viewsets.ModelViewSet):
    # Queryset que devuelve todos los objetos de Programas_Rutas
    queryset = Programas_Rutas.objects.all()

    # Serializador que se usa para validar y transformar los datos
    serializer_class = Programas_RutasSerializers

# importarlas en init y en urls para que pueda funcionar
