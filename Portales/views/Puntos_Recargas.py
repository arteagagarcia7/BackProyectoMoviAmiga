from rest_framework import viewsets

# importo el modelo creado que corresponde
from Portales.models import Puntos_Recargas

# importo el serializador creado que corresponde
from Portales.serializers import Puntos_RecargasSerializers


# crear la vista
class Puntos_RecargasViewset(viewsets.ModelViewSet):
    queryset = Puntos_Recargas.objects.all()
    serializer_class = Puntos_RecargasSerializers

# importarlas en init y en urls para que pueda funcionar
