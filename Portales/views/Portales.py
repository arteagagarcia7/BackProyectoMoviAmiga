from rest_framework import viewsets
from rest_framework.response import Response

# Importo el modelo y el serializador correspondiente
from Portales.models import Portales
from Portales.serializers import PortalesSerializers


# Crear la vista
class PortalesViewset(viewsets.ModelViewSet):
    queryset = Portales.objects.all()
    serializer_class = PortalesSerializers

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
