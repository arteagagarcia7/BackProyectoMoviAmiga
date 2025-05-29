from rest_framework import viewsets

# importo el modelo creado que corresponde
from Portales.models import Paraderos

# importo el serializador creado que corresponde
from Portales.serializers import ParaderosSerializers


# crear la vista
class ParaderosViewset(viewsets.ModelViewSet):
    queryset = Paraderos.objects.all()
    serializer_class = ParaderosSerializers

# importarlas en init y en urls para que pueda funcionar
