from rest_framework import viewsets

# mi modelo creado
from Usuarios.models import Tarjeta_Usuario

# mi serializador creado
from Usuarios.serializers import Tarjeta_UsuarioSerializer


class Tarjeta_UsuarioViewset(viewsets.ModelViewSet):
    queryset = Tarjeta_Usuario.objects.all()
    serializer_class = Tarjeta_UsuarioSerializer
