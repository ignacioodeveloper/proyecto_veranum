from django.db import models

# Create your models here.

# TIPO SERVICIO
class TipoServicio(models.Model):

    nombre = models.TextField(max_length=100)
    descripcion = models.TextField(max_length=100)
    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'tipo_servicio'
        verbose_name = 'Tipo de Servicio'
        verbose_name_plural = 'Tipos de Servicios'

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=100)
    tipo_servicio = models.ForeignKey(TipoServicio, on_delete=models.SET_NULL, null=True, blank=True)
    disponible = models.BooleanField(default=True) 
    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'servicio'
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'

# HOTEL
class Hotel(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    comuna = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20)
    cantidad_habitaciones = models.PositiveIntegerField()
    telefono_hotel = models.CharField(max_length=15)
    correo_hotel = models.EmailField()
    descripcion_hotel = models.TextField(blank=True, null=True)
    servicio = models.ForeignKey(Servicio,on_delete=models.SET_NULL, null=True,blank=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'hotel'
        verbose_name = 'Hotel'
        verbose_name_plural = 'Hoteles'
        ordering = ['id']
