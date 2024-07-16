from rest_framework import serializers
from .models import Edificio, Departamento

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'

class EdificioSerializer(serializers.ModelSerializer):
    departamentos = DepartamentoSerializer(many=True, read_only=True)

    class Meta:
        model = Edificio
        fields = '__all__'