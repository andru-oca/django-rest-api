from django.db import models

class Pelicula(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    fecha_de_release = models.DateField()
    genero = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        db_table = 'pelicula'