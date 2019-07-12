from django.db import models
class imagenPerfil(models.Model):
    titulo = models.TextField()
    imagen = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.titulo
# Create your models here.
