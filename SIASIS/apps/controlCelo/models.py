from django.db import models

# Create your models here.
class celo (models.Model):
    fechaInicioCelo = models.DateField()
    fechaFinCelo = models.DateField()
    fechaAplic = models.DateField()
    nombreVacuna = models.CharField(max_length = 60)
    