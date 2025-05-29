from rest_framework import viewsets

# importo el modelo creado que corresponde
from Portales.models import Rutas_PuntosRecargas

# importo el serializador creado que corresponde
from Portales.serializers import Rutas_PuntosRecargasSerializers

# crear la vista


class Rutas_PuntosRecargasViewset(viewsets.ModelViewSet):
    queryset = Rutas_PuntosRecargas.objects.all()
    serializer_class = Rutas_PuntosRecargasSerializers

# importarlas en init y en urls para que pueda funcionar
