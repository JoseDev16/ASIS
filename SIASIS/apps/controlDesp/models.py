from django.db import models
from apps.registroMascota.models import Expediente
# Create your models here.
class Desparasitante(models.Model):
    nombreDesparasitante = models.CharField(max_length = 60)

class ControlDesparasitacion(models.Model):
    fechaAplicacion=models.DateField()
    fechaProxDes= models.DateField()
    dosisDesp = models.IntegerField()
    desparasitante = models.ForeignKey(Desparasitante, null = True, blank = True, on_delete = models.CASCADE)
    expediente = models.ForeignKey(Expediente,null = True, blank = True, on_delete =models.CASCADE)

