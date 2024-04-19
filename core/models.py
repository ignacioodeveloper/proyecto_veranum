from django.db import models
# importacion authenticaion de usuario por django
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

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

# servicio
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

    # relacion 1:M hotel puede tener muchos servicios
    servicios = models.ManyToManyField(Servicio, related_name='hoteles')

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'hotel'
        verbose_name = 'Hotel'
        verbose_name_plural = 'Hoteles'
        ordering = ['id']

# Tipo de Habitacion
class TipoHabitacion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

# Servicio Habitacion
class ServicioHabtacion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

# Habitacion
class Habitacion(models.Model):
    id = models.AutoField(primary_key=True)
    tipo_habitacion = models.ForeignKey(TipoHabitacion, on_delete=models.CASCADE)
    capacidad = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponibilidad = models.BooleanField(default=True)
    servicios_habitacion = models.ManyToManyField(ServicioHabtacion, related_name='habitaciones')

    def __str__(self):
        return f"Habitación {self.id} ({self.nombre})"

    class Meta:
        db_table = 'habitacion'
        verbose_name = 'Habitacion'
        verbose_name_plural = 'Habitaciones'
        ordering = ['id']

# Usuario
# class Usuario(AbstractUser):
#     id_usuario = models.AutoField(primary_key=True)  # Identificador único del usuario
#     direccion = models.CharField(max_length=200)  # Dirección del cliente
#     telefono = models.CharField(max_length=15)  # Número de teléfono del cliente
#     email = models.EmailField(unique=True)  # Correo electrónico del cliente (único)
#     fecha_nacimiento = models.DateField(null=True, blank=True)  # Fecha de nacimiento del cliente
#     preferencias = models.TextField(blank=True)  # Preferencias del cliente (por ejemplo, tipo de habitación, servicios adicionales, etc.)

#     # Campos relacionados con la autenticación (proporcionados por Django)
#     username = models.CharField(max_length=150, unique=True)
#     password = models.CharField(max_length=128)

#     # Campos para seguridad y funcionalidad
#     is_active = models.BooleanField(default=True)  # Indica si el usuario está activo
#     last_login = models.DateTimeField(null=True, blank=True)  # Fecha y hora del último inicio de sesión

#     def __str__(self):
#         return self.username

#     class Meta:
#         db_table = 'user'
#         verbose_name = 'Usuario'
#         verbose_name_plural = 'Usuarios'
#         ordering = ['id_usuario']

# class Administrador(Usuario):
#     id_admin = models.AutoField(primary_key=True)  # Identificador único del usuario
#     nivel_acceso = models.PositiveIntegerField()

#     class Meta:
#         db_table = 'administrador'
#         verbose_name = 'Administrador'
#         verbose_name_plural = 'Administradores'

# class Superusuario(Usuario):
#     id_superuser = models.AutoField(primary_key=True)  # Identificador único del usuario
#     permisos_especiales = models.BooleanField(default=True)

#     class Meta:
#         db_table = 'superusuario'
#         verbose_name = 'Superusuario'
#         verbose_name_plural = 'Superusuarios'

class EstadoReserva(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField(blank=True)

# Reservas
class Reserva(models.Model):
    estado = models.ForeignKey(EstadoReserva, on_delete=models.SET_NULL, null=True, blank=True)

    id = models.AutoField(primary_key=True)
    check_in = models.DateField()
    check_out = models.DateField()
    cliente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservas_cliente')
    pasajeros = models.PositiveIntegerField()
    id_habitacion = models.ForeignKey('Habitacion', on_delete=models.CASCADE, related_name='reservas_habitacion')
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)

    fecha_reserva = models.DateTimeField(auto_now_add=True)
    servicios_extra = models.ManyToManyField(Servicio, related_name='reservas')
    def __str__(self):
        return f"Reserva {self.id} - Cliente: , Habitación: {self.id_habitacion}"
