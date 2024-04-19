from django.contrib import admin
from .models import TipoServicio,Servicio,Hotel,TipoHabitacion,ServicioHabtacion,Habitacion,Reserva
# Register your models here.


admin.site.register(Hotel)
admin.site.register(Servicio)
admin.site.register(TipoServicio)
admin.site.register(TipoHabitacion)
admin.site.register(ServicioHabtacion)
admin.site.register(Habitacion)
# admin.site.register(Usuario)
# admin.site.register(Administrador)
# admin.site.register(Superusuario)
admin.site.register(Reserva)
