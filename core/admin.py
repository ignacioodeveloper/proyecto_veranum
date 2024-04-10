from django.contrib import admin
from .models import Hotel,Servicio,TipoServicio
# Register your models here.


admin.site.register(Hotel)
admin.site.register(Servicio)
admin.site.register(TipoServicio)