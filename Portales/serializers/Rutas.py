# importar de django restframework el serializador y el modelo
from rest_framework import serializers
from Portales.models import Rutas


# crear el serializador
class RutasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rutas
        fields = '__all__'

# importar el modelo en el init para que pueda funcionar en las demás carpetas
