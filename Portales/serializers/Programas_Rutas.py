# importar de django restframework el serializador y el modelo
from rest_framework import serializers
from Portales.models import Programas_Rutas


# crear el serializador
class Programas_RutasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Programas_Rutas
        fields = '__all__'

# importar el modelo en el init para que pueda funcionar en las demás carpetas
