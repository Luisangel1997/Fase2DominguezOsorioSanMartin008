from django.db import models
from django.urls import reverse 
import uuid

# Create your models here.

class Usuarios(models.Model):
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    email=models.EmailField()
    telefono=models.IntegerField(max_length=9)

	class Meta:
		ordering = ['nombre']

	def __str__(self):
		"""String for representing the Model object."""
		return self.nombre

class Productos(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    nombreProductos=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=200)
    precio=models.IntegerField(max_length=9)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

	class Meta:
		ordering = ['id']

	def __str__(self):
		"""String for representing the Model object."""
		return self.id

