from django.db import models

from apps.registroMascota.models import Expediente



# Create your models here.

class Vacuna(models.Model):
    nombre = models.CharField(max_length = 60)

class ControlVacuna(models.Model):
    fechaAplicacionVac = models.DateField()
    nombreProxVac = models.CharField(max_length  = 60)
    fechaProxVac = models.DateField()
    cantDosis = models.IntegerField()
    vacu = models.ForeignKey(Vacuna, null = True, blank = True, on_delete =models.CASCADE)
    expediente = models.ForeignKey(Expediente,null = True, blank = True, on_delete =models.CASCADE)


