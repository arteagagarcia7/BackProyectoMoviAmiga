from rest_framework import viewsets

# importo el modelo creado que corresponde
from Portales.models import Buses

# importo el serializador creado que corresponde
from Portales.serializers import BusesSerializers


# crear la vista
class BusesViewset(viewsets.ModelViewSet):
    queryset = Buses.objects.all()
    serializer_class = BusesSerializers

# importarlas en init y en urls para que pueda funcionar
