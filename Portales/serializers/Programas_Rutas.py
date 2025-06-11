# importar de django restframework el serializador y el modelo
from rest_framework import serializers
from Portales.models import Programas_Rutas


# crear el serializador
class Programas_RutasSerializers(serializers.ModelSerializer):
    # Campos adicionales para mostrar el nombre de los portales relacionados
    # con las llaves foraneas en el front
    # Estos campos son de solo lectura y usan el atributo 'source' para
    # obtener el nombre desde las llaves foráneas
    portal_origen_nombre = serializers.CharField(
        source='portal_origen.nombre', read_only=True)
    portal_final_nombre = serializers.CharField(
        source='portal_final.nombre', read_only=True)

    class Meta:
        model = Programas_Rutas
        # Incluye todos los campos del modelo, además de los dos nuevos campos
        # con nombres legibles
        fields = '__all__'
        # Esto significa que el serializer enviará todos los campos, incluidos
        # los IDs de portal y sus nombres para el front

# importar el modelo en el init para que pueda funcionar en las demás carpetas
