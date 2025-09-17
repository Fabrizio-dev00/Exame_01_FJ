from django.db import models

class Autores(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
    
class Articulos(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=200)
    fecha_publicacion = models.DateField()
    autores = models.ForeignKey(Autores, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo