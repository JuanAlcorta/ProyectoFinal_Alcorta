from django import forms

class CargaClub(forms.Form):
    nombreClub = forms.CharField(max_length=50)
    nombreEstadio = forms.CharField(max_length=50)
    direccionEstadio = forms.CharField(max_length=50)
    capacidadEstadio = forms.IntegerField()
    fechaFundacion = forms.DateField()
    localidad = forms.CharField(max_length=50)
    provincia = forms.CharField(max_length=50)
    fotoEstadio = forms.ImageField()
    historia = forms.CharField(widget=forms.Textarea)
    

class CargaSocio(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    dni = forms.IntegerField()
    email = forms.EmailField()

class CargaPartido(forms.Form):
    equipoLocal = forms.CharField(max_length=50)
    equipoVisitante = forms.CharField(max_length=50)
    fechaPartido = forms.DateField()
    horarioPartido = forms.TimeField()
    
    