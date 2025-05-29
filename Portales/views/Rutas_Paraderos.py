from rest_framework import viewsets

# importo el modelo creado que corresponde
from Portales.models import Rutas_Paraderos

# importo el serializador creado que corresponde
from Portales.serializers import Rutas_ParaderosSerializers


# crear la vista
class Rutas_ParaderosViewset(viewsets.ModelViewSet):
    queryset = Rutas_Paraderos.objects.all()
    serializer_class = Rutas_ParaderosSerializers

# importarlas en init y en urls para que pueda funcionar
