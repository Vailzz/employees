from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class Employee(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    version = models.IntegerField()
    manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    def get_hierarchy(self):
        hierarchy = [{'name': self.name, 'position': self.position, 'version': self.version}]
        for subordinate in self.employee_set.all():
            hierarchy.append(subordinate.get_hierarchy())
        return hierarchy