# importar de django restframework el serializador y el modelo
from rest_framework import serializers
from Portales.models import Portales


# crear el serializador
class PortalesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Portales
        fields = '__all__'

# importar el modelo en el init para que pueda funcionar en las demás carpetas
