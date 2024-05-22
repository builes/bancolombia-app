from django.db import models


class Actor(models.Model):
    nombre = models.CharField(max_length=255)
    edad = models.IntegerField()
    genero = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Pose(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre




class Ubicacion(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)    
    # escena = models.ForeignKey('guion.Escena', on_delete=models.CASCADE)
    coordenada_x = models.FloatField()
    coordenada_y = models.FloatField()
    coordenada_z = models.FloatField()
    rotacion_x = models.FloatField()
    rotacion_y = models.FloatField()
    rotacion_z = models.FloatField()

    




