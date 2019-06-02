from django.db import models

# Create your models here.
class Consulta(models.Model):
    titulo = models.CharField(max_length = 100)
    detalleConsulta = models.TextField()
    medicamento = models.TextField()
    proximaCita = models.DateField()
    citaunica = models.BooleanField()


