from rest_framework import viewsets

# importo el modelo creado que corresponde
from Portales.models import Programas_Rutas

# importo el serializador creado que corresponde
from Portales.serializers import Programas_RutasSerializers


# crear la vista
class Programas_RutasViewset(viewsets.ModelViewSet):
    queryset = Programas_Rutas.objects.all()
    serializer_class = Programas_RutasSerializers

# importarlas en init y en urls para que pueda funcionar
