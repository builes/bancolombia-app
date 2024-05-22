from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Guion(models.Model):
    titulo = models.CharField(max_length=255)
    genero = models.CharField(max_length=100)
    usuario = models.ForeignKey('usuario.Usuario', on_delete=models.CASCADE, related_name='guiones_escritos')
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
    def create_historial_cambios(self, usuario):
        HistorialCambios.objects.create(
            guion=self,
            usuario=usuario
        )
        print(usuario)

    


class Escena(models.Model):
    guion = models.ForeignKey(Guion, on_delete=models.CASCADE, related_name='escenas')
    numero_escena = models.PositiveIntegerField()
    descripcion = models.TextField()
    actores = models.ManyToManyField('actor.Actor', related_name='escenas')

    def __str__(self):
        return f"Escena {self.numero_escena} - Guion: {self.guion.titulo}"

class Dialogo(models.Model):
    escena = models.ForeignKey(Escena, on_delete=models.CASCADE, related_name='dialogos')
    texto = models.TextField()

    # un dialogo pertenece a un actor
    actor  = models.ForeignKey('actor.Actor', on_delete=models.CASCADE, null=True)  # Permitir valores nulos temporalmente)

    def __str__(self):
        return f"Dialogo de {self.actor} en la Escena {self.escena.numero_escena}"

class HistorialCambios(models.Model):
    guion = models.ForeignKey(Guion, on_delete=models.CASCADE, related_name='historial_cambios')
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey('usuario.Usuario', on_delete=models.CASCADE, related_name='guiones')
    

    def __str__(self):
        return f"Historial de cambios de {self.guion.titulo} - {self.fecha}"

@receiver(post_save, sender=Guion)
def crear_historial_cambios_guion(sender, instance, created, **kwargs):
    if created:
        # Si se crea un nuevo guion, no hay historial de cambios que crear
        return
    
    # Si el guion ya existía y se está modificando, creamos el historial de cambios
    if instance.usuario:
        # Solo creamos el historial de cambios si el usuario está definido
        instance.create_historial_cambios(usuario=instance.usuario)