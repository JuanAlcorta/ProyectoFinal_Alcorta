from django.db import models
from django.utils import timezone

# Create your models here.

class Mensaje(models.Model):
    autorMensaje = models.CharField(max_length=100)
    texto = models.TextField(null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)

    

