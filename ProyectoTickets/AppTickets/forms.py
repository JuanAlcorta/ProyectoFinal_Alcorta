from django import forms
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User

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

class FormEdicionPerfil(UserChangeForm):
    username = forms.CharField(widget= forms.TextInput(attrs={"placeholder":"Username"}))
    email = forms.CharField(widget= forms.TextInput(attrs={"placeholder":"Email"}))
    first_name = forms.CharField(widget= forms.TextInput(attrs={"placeholder":"First Name"}))
    last_name = forms.CharField(widget= forms.TextInput(attrs={"placeholder":"Last Name"}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name'] 
        help_texts = {k:"" for k in fields}

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label = "", widget= forms.PasswordInput(attrs={"placeholder":"Old password"}))
    new_password1 = forms.CharField(label = "", widget= forms.PasswordInput(attrs={"placeholder":"New password"}))
    new_password2 = forms.CharField(label = "", widget= forms.PasswordInput(attrs={"placeholder":"Confirmation new password"}))

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
        help_texts = {k:"" for k in fields}   


class AvatarForm(forms.Form):
    avatar = forms.ImageField()
    linkInfo = forms.URLField(max_length=200)
    descripcion = forms.CharField(widget=forms.Textarea)
    