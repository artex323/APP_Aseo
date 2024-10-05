
from django.contrib import admin
from .models import Cliente, Empleado, Servicio, Reserva, Factura

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Empleado)
admin.site.register(Servicio)
admin.site.register(Reserva)
admin.site.register(Factura)


