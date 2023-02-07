from django.db import models

# Create your models here.
class Productos(models.Model):
    nombre = models.CharField(max_length=60)
    descripcion = models.TextField(max_length=600)
    departamento = models.CharField(max_length=60)
    talla = models.CharField(max_length=20)
    color = models.CharField(max_length=60)
    tipo = models.CharField(max_length=60)
    existencia = models.IntegerField()
    imagen = models.ImageField(null=True, height_field=100, width_field=100)

class Clientes(models.Model):
    nombre = models.CharField(max_length=60)
    edad = models.IntegerField()
    correo = models.EmailField()
    calleYNumero = models.TextField(max_length=100)
    colonia = models.CharField(max_length=60)
    municipio = models.CharField(max_length=60)
    estado = models.CharField(max_length=60)
    pais = models.CharField(max_length=60)
    cp = models.IntegerField()

class Carrito(models.Model):
    producto = models.IntegerField()
    precio = models.DecimalField(max_digits=10,decimal_places=2)
    cantidad = models.IntegerField()
    iva = models.DecimalField(max_digits=10,decimal_places=2)

