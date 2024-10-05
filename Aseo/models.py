from django.db import models

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre_cliente = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre_cliente

class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    nombre_empleado = models.CharField(max_length=100)
    telefono = models.IntegerField()
    email = models.EmailField()
    cargo = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_empleado

class Servicio(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.FloatField()

    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    fecha = models.CharField(max_length=100)  
    hora = models.CharField(max_length=100)  
    telefono = models.IntegerField()
    id_servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    id_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f"Reserva {self.id_reserva} - {self.fecha}"

class Factura(models.Model):
    id_factura = models.AutoField(primary_key=True)
    fecha = models.CharField(max_length=100) 
    monto_total = models.FloatField()
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)

    def __str__(self):
        return f"Factura {self.id_factura} - {self.monto_total}"
