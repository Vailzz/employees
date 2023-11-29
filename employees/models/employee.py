from django.db import models
class Empleado(models.Model):

    nombre = models.CharField(max_length=100)
    posicion = models.CharField(max_length=100)
    version = models.IntegerField(default=1)
    superior_jerarquico = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre

    def get_jerarquia(self):
        jerarquia = [self]
        superior = self.superior_jerarquico
        while superior:
            jerarquia.insert(0, superior)
            superior = superior.superior_jerarquico
        return jerarquia

    def actualizar_jefe(self, nuevo_jefe):
        if self.superior_jerarquico != nuevo_jefe:
            self.superior_jerarquico = nuevo_jefe
            self.version += 1
            self.save()