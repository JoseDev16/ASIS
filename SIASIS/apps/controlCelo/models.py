from django.db import models

from apps.registroMascota.models import Expediente
# Create your models here.
class Celo (models.Model):
    nombreVacunaCelo = models.CharField(max_length = 60)
    def __str__(self):
        return self.nombreVacunaCelo


class ControlCelo (models.Model):
    fechaInicioCelo = models.DateField(unique=True)
    fechaFinCelo = models.DateField(unique=True)
    fechaAplic = models.DateField(unique=True)
    celo = models.ForeignKey(Celo, null = True, blank = True, on_delete = models.CASCADE)
    

