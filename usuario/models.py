from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
    
    

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=128)  
    
    roles = [
        # el primer valor es el que se guarda en la base de datos
        # el segundo valor es el que se muestra en el formulario
        ('guionista', 'Guionista'),
        ('usuario', 'Usuario'),
    ]

    rol = models.CharField(max_length=20, choices=roles, default='usuario')


    # este metodo se llama automaticamente cada vez que se guarda un 
    # objeto en la base de datos
    def save(self, *args, **kwargs):
        # Ciframos la contraseña antes de guardarla
        self.contrasena = make_password(self.contrasena)
        super(Usuario, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombre