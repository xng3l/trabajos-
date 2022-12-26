from django.db import models

class Servicio(models.Model):
     id=models.IntegerField(primary_key=True)
     nombre = models.CharField(max_length=35)
     tipoServicio = models.CharField(max_length=35)
     nombreEmpresa = models.CharField(max_length=35)
     direccion = models.CharField(max_length=35)
     contacto = models.IntegerField()
     correo = models.EmailField(max_length=254)
     def __str__(self):
          return self.nombre
class Cliente(models.Model):
    id=models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=35)
    apellido = models.CharField(max_length=35)
    edad = models.IntegerField()
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    correo = models.EmailField(max_length=254)
    formapago = models.CharField(max_length=50)
    def __str__(self):
          return  self.nombre

class Subscripcion(models.Model):
     id=models.IntegerField(primary_key=True)
     cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE )
     servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE )
     Subscripcion_type = models.CharField(max_length=10)
     created_at = models.DateTimeField()
     precio = models.IntegerField()
     finish = models.DateTimeField()