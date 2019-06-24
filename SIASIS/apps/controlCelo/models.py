from django.db import models

from apps.registroMascota.models import Expediente
# Create your models here.
class Celo (models.Model):
    nombreVacunaCelo = models.CharField(max_length = 60)
    def __str__(self):
        return self.nombreVacunaCelo


class ControlCelo (models.Model):
    fechaInicioCelo = models.DateField()
    fechaFinCelo = models.DateField()
    fechaAplic = models.DateField()
    proximoCelo = models.DateField(null=True)
    celo = models.ForeignKey(Celo, null = True, blank = True, on_delete = models.CASCADE)
    expediente = models.ForeignKey(Expediente, null = True, blank = True, on_delete = models.CASCADE)