from rest_framework import viewsets

# mi modelo creado
from Usuarios.models import Ruta_Favorita

# mi serializador creado
from Usuarios.serializers import Ruta_FavoritaSerializer


class Ruta_FavoritaViewset(viewsets.ModelViewSet):
    queryset = Ruta_Favorita.objects.all()
    serializer_class = Ruta_FavoritaSerializer
