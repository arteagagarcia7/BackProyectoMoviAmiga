from rest_framework import viewsets

# mi modelo creado
from Usuarios.models import Plan_Viaje

# mi serializador creado
from Usuarios.serializers import Plan_ViajeSerializer


class Plan_ViajeViewset(viewsets.ModelViewSet):
    queryset = Plan_Viaje.objects.all()
    serializer_class = Plan_ViajeSerializer
