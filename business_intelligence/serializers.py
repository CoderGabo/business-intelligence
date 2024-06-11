# serializers.py

from rest_framework import serializers
from .models import Servicio, ServicioMantenimiento

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = ['name', 'description', 'cost']

# class ServicioMantenimientoSerializer(serializers.ModelSerializer):
#     servicio_nombre = serializers.CharField(source='service.name')
#     servicio_descripcion = serializers.CharField(source='service.description')
#     servicio_costo = serializers.DecimalField(source='service.cost', max_digits=10, decimal_places=2)

#     class Meta:
#         model = ServicioMantenimiento
#         fields = ['servicio_nombre', 'servicio_descripcion', 'servicio_costo']
