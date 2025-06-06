from rest_framework import serializers
from Usuarios.models import Tarjeta_Usuario


class Tarjeta_UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarjeta_Usuario
        fields = '__all__'
