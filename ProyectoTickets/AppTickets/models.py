from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Socio(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.IntegerField()
    email = models.EmailField()
    def __str__(self):
        return f"nombre: {self.nombre} - apellido: {self.apellido} - dni: {self.dni} - email: {self.email}"

class Club(models.Model):
    nombreClub = models.CharField(max_length=50)
    nombreEstadio = models.CharField(max_length=50)
    direccionEstadio = models.CharField(max_length=50)
    fechaFundacion = models.DateField(null=True)
    localidad = models.CharField(max_length=50, null=True)
    provincia = models.CharField(max_length=50, null=True)
    capacidadEstadio = models.IntegerField(null=True)
    fotoEstadio = models.ImageField(upload_to='imagenesClubes', null=True, blank=True)
    historia = models.TextField(null=True)
    #autorid = models.ForeignKey(User, on_delete=models.CASCADE,null = True, blank = True)
    autorNombre = models.CharField(max_length=50,null = True, blank = True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
        
    def __str__(self):
        return f"Club: {self.nombreClub} - Estadio: {self.nombreEstadio} - Direccion: {self.direccionEstadio} - Capacidad: {self.capacidadEstadio}"

class Partido(models.Model):
    equipoLocal = models.CharField(max_length=50)
    equipoVisitante = models.CharField(max_length=50)
    fechaPartido = models.DateField()
    horarioPartido = models.TimeField()
    def __str__(self):
        return f"Local: {self.equipoLocal} - Visitante: {self.equipoVisitante} - Fecha: {self.fechaPartido} - Hora: {self.horarioPartido}"

class Avatar(models.Model):
    #vinculo con el usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #SubCarpeta de avatares
    image = models.ImageField(upload_to='avatares', null = True, blank = True)
    linkInfo = models.URLField(max_length=200,null=True,blank=True)
    descripcion = models.TextField(null=True,blank=True)