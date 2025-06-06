from rest_framework import serializers
from Usuarios.models import Ruta_Favorita


class Ruta_FavoritaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ruta_Favorita
        fields = '__all__'
