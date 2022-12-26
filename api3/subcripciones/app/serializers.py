from rest_framework import serializers
from app.models import Servicio, Subscripcion, Cliente

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model= Servicio
        fields='__all__'
        
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model= Cliente
        fields='__all__'
        
class SubscripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Subscripcion
        fields='__all__'