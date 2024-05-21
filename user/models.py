from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Animal (models.Model):
    idAnimal = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    raza = models.CharField(max_length=30)
    estadoActual = models.BooleanField(default=True)
    estadoSalud = models.CharField(max_length=30)
    ubicacion = models.CharField(max_length=30)
    fechaRescate = models.DateField(null=True, blank=True)
    fechaAdopcion = models.DateField(null=True, blank=True)
    numeroContacto = models.PositiveIntegerField(null=True, blank=True)
    imagenAnimal = models.ImageField(null=True, blank=True, upload_to='fotos')

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.raza)
    
class Aliado (models.Model):
    idAliado = models.AutoField(primary_key=True)
    nombre_empresa = models.CharField(max_length=30, verbose_name= 'Nombre de la empresa')
    correo = models.CharField(max_length=30, verbose_name= 'Correo de la empresa')
    contraseña = models.CharField(max_length=30, verbose_name= 'Contraseña')
    telefono = models.CharField(max_length=30, verbose_name= 'Telefono de la empresa')
    ofrece = models.CharField(max_length=30, verbose_name= 'Producto o servicios')
    categoria = models.CharField(max_length=30, verbose_name= 'Tipo de productos')
    imagenAliado = models.ImageField(null=True, blank=True, upload_to='fotos')

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre_empresa, self.correo)
    

class Consejos (models.Model):
    idConsejo = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)
    imagenConsejo = models.ImageField(null=True, blank=True, upload_to='fotos')

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.titulo, self.descripcion)