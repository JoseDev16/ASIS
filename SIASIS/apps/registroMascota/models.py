from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class DueñoMascota (models.Model):
    nombres = models.CharField(max_length = 50,null = True)
    apellidos = models.CharField(max_length = 50,null = True)
    fechaNacDueno = models.DateField(null = True)
    direccion = models.CharField(max_length = 200)
    telefono = models.IntegerField()
    celular = models.IntegerField()
    correo = models.EmailField(null = True)
    cuenta = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)



class Mascota(models.Model):
    nombre= models.CharField(max_length= 30)
    raza= models.CharField(max_length= 30)
    sexo = models.CharField(max_length = 1)
    fechaNacimiento = models.DateField()
    razaPadre = models.CharField(max_length = 30)
    razaMadre = models.CharField(max_length = 30)
    peso = models.FloatField()
    dueñomascota = models.ForeignKey(DueñoMascota, null = True, blank = True, on_delete = models.CASCADE)

    def __str__(self):
        return self.nombre
    



    

class Expediente(models.Model):
    inicioControl = models.DateField(auto_now_add = True)
    mascota = models.ForeignKey(Mascota, null= True, blank = True, on_delete = models.CASCADE)
    

