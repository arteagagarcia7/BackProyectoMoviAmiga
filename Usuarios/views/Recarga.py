from rest_framework import viewsets

# mi modelo creado
from Usuarios.models import Recarga

# mi serializador creado
from Usuarios.serializers import RecargaSerializer


class RecargaViewset(viewsets.ModelViewSet):
    queryset = Recarga.objects.all()
    serializer_class = RecargaSerializer
