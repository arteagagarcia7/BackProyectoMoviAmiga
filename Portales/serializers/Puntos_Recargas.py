# importar de django restframework el serializador y el modelo
from rest_framework import serializers
from Portales.models import Puntos_Recargas


# crear el serializador
class Puntos_RecargasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Puntos_Recargas
        fields = '__all__'

# importar el modelo en el init para que pueda funcionar en las demás carpetas
