from employees.models.employee import Empleado
from rest_framework import serializers

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'