from django.http import JsonResponse
from employees.models.employee import Empleado
from django.shortcuts import get_object_or_404
from rest_framework import status, views

class employeeCreateView(views.APIView):
    def jerarquia_empleados(request):
        empleados = Empleado.objects.all()
    
        def build_hierarchy(emp):
            return {
                'nombre': emp.nombre,
                'posicion': emp.posicion,
                'version': emp.version,
                'superior_jerarquico': build_hierarchy(emp.superior_jerarquico) if emp.superior_jerarquico else None
            }
    
        jerarquia = []
        for empleado in empleados:
            if not empleado.superior_jerarquico:
                jerarquia.append(build_hierarchy(empleado))
    
        return JsonResponse({'jerarquia_empleados': jerarquia})
    
    def actualizar_jefe(request, empleado_id, nuevo_jefe_id):
        empleado = get_object_or_404(Empleado, pk=empleado_id)
        nuevo_jefe = get_object_or_404(Empleado, pk=nuevo_jefe_id)
    
        empleado.actualizar_jefe(nuevo_jefe)
    
        return JsonResponse({'mensaje': f"El empleado {empleado.nombre} ha sido actualizado correctamente."})