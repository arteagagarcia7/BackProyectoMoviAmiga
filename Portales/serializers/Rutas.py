from rest_framework import serializers
# Asegúrate de importar todos
from Portales.models import Rutas, Buses, Programas_Rutas


class RutasSerializers(serializers.ModelSerializer):

    codigo_bus = serializers.CharField(
        source='buses.codigo_bus', read_only=True)
    buses = serializers.SlugRelatedField(
        queryset=Buses.objects.all(),
        slug_field='codigo_bus'
    )

    # Mostrar nombres de portales desde programas_Rutas para seleccionarlos
    # en el front ya que tiene llave foranea de programas_rutas y se pueden
    # obtener datos de portales de ahí
    portal_origen_nombre = serializers.CharField(
        source='programas_Rutas.portal_origen.nombre', read_only=True)
    portal_final_nombre = serializers.CharField(
        source='programas_Rutas.portal_final.nombre', read_only=True)

    programas_Rutas = serializers.PrimaryKeyRelatedField(
        queryset=Programas_Rutas.objects.all()
    )

    class Meta:
        model = Rutas
        fields = '__all__'
