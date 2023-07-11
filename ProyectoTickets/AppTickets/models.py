from django.db import models

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

