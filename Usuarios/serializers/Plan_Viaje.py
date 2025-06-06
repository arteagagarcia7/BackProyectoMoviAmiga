from rest_framework import serializers
from Usuarios.models import Plan_Viaje


class Plan_ViajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan_Viaje
        fields = '__all__'
