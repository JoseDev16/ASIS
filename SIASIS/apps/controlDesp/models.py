from django.db import models

# Create your models here.
class Desparasitacion(models.Model):
    nombreDesparasitante = models.CharField(max_length = 60)
    fechaAplicacion=models.DateField()
    fechaProxDes= models.DateField()
    dosisDesp = models.IntegerField()
    
