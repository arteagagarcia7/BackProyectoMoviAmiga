from rest_framework import viewsets

# importo el modelo creado que corresponde
from Portales.models import Rutas

# importo el serializador creado que corresponde
from Portales.serializers import RutasSerializers

# crear la vista


class RutasViewset(viewsets.ModelViewSet):
    queryset = Rutas.objects.all()
    serializer_class = RutasSerializers

# importarlas en init y en urls para que pueda funcionar
