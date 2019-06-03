from django.db import models

from apps.registroMascota.models import Expediente
# Create your models here.
class Celo (models.Model):
    nombreVacunaCelo = models.CharField(max_length = 60)


class ControlCelo (models.Model):
    fechaInicioCelo = models.DateField()
    fechaFinCelo = models.DateField()
    fechaAplic = models.DateField()
    celo = models.ForeignKey(Celo, null = True, blank = True, on_delete = models.CASCADE)
    

