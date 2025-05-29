# importar de django restframework el serializador y el modelo
from rest_framework import serializers
from Portales.models import Paraderos


# crear el serializador
class ParaderosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Paraderos
        fields = '__all__'

# importar el modelo en el init para que pueda funcionar en las demás carpetas
