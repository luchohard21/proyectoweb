from django.db import models
from django.db.models.fields import CharField

# Create your models here.
#creacion tabla de clientes de urbanstyle
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    rut = models.CharField(max_length=9)
    fono = models.CharField(max_length=9)

class Tipo_servicio(models.Model):
    valor_servicio = models.CharField(int=6)
    nombre_servicio = models.CharField(max_length=20)
    puntos_servicio = models.CharField(int = 2)    

class Servicio(models.Model):
    Tipo_servicio = models.ForeignKey(Tipo_servicio, on_delete=models.PROTECT)


class Empleado (models.Model):
    nombre = models.CharField(max_length=50)
    rut = models.CharField(int = 9)
    fono = models.CharField(int = 9)
    email = models.CharField(max_length=20) 
    especialidad = models.CharField(max_length=20)

class DetalleCita(models.Model):
    fecha = models.DateField()
    hora = models.DateTimeField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    Cita = models.ForeignKey(Cita, on_delete=models.CASCADE)



class Cita(models.Model):
    nombre_servicio = models.ForeignKey(Tipo_servicio, on_delete= models.PROTECT)
    nombre = models.ForeignKey(Empleado, on_delete= models.PROTECT)


class Detalle_Servicio(models.Model):
    Cita = models.ForeignKey(Cita, on_delete=models.PROTECT)
    Servicio = models.ForeignKey(Servicio, on_delete=models.PROTECT)


class Pago(models.Model):
    Tipo_de_pago = models.CharField(max_length=10)
    Servicio = models.ForeignKey(Servicio, on_delete=models.PROTECT)



class Club(models.Model):
    Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    Servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    total_puntos_cliente = models.CharField(int = 2) 

class Detalle_servicio_empleado(models.Model):
    Servicio = models.ForeignKey(Servicio, on_delete=models.PROTECT)
    Empleado = models.ForeignKey(Empleado, on_delete=models.PROTECT)


class Especialidad(models.Model):
    nombre_especialidad = models.CharField(max_length=20)

