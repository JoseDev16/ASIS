from django.db import models
from apps.registroMascota.models import Expediente

# Create your models here.
class Consulta(models.Model):
    titulo = models.CharField(max_length = 100)
    detalleConsulta = models.TextField()
    medicamento = models.TextField()
    proximaCita = models.DateField()
    citaunica = models.BooleanField()
    expediente = models.ForeignKey(Expediente,null = True, blank = True, on_delete =models.CASCADE)


