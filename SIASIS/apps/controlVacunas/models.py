from django.db import models

# Create your models here.
class Vacuna(models.Model):
    nombre = models.CharField(max_length = 60)
    fechaAplicacionVac = models.DateField()
    nombreProxVac = models.CharField(max_length  = 60)
    fechaProxVac = models.DateField()
    cantDosis = models.IntegerField()
