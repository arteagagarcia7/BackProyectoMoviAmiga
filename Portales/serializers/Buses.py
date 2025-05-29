# importar de django restframework el serializador y el modelo
from rest_framework import serializers
from Portales.models import Buses


# crear el serializador
class BusesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Buses
        fields = '__all__'

# importar el modelo en el init para que pueda funcionar en las demás carpetas
