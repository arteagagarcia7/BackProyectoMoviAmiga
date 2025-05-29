from rest_framework import viewsets

# importo el modelo creado que corresponde
from Portales.models import Portales

# importo el serializador creado que corresponde
from Portales.serializers import PortalesSerializers


# crear la vista
class PortalesViewset(viewsets.ModelViewSet):
    queryset = Portales.objects.all()
    serializer_class = PortalesSerializers

# importarlas en init y en urls para que pueda funcionar
