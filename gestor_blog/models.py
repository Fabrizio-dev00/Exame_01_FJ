from django.db import models

class Articulos(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=200)
    fecha_publicacion = models.DateField()

    def __str__(self):
        return self.titulo

class Autores(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre