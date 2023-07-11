from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppTickets.forms import *
from AppTickets.models import *
from datetime import datetime
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def inicio(request):
    return render(request, "AppTickets/inicio.html")

@login_required
def socios(request):
    if request.method == 'POST':
        miFormulario = CargaSocio(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            socio = Socio(nombre=informacion["nombre"],apellido=informacion["apellido"],dni=informacion["dni"],email=informacion["email"])
            socio.save()
            miFormulario=CargaSocio()
            return render(request,"AppTickets/socios.html",{"miFormulario":miFormulario})
    else:
        miFormulario = CargaSocio()
    return render(request, "AppTickets/socios.html",{"miFormulario":miFormulario})

@login_required
def partidos(request):
    if request.method == 'POST':
        miFormulario = CargaPartido(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            partido = Partido(equipoLocal=informacion["equipoLocal"],equipoVisitante=informacion["equipoVisitante"],fechaPartido=informacion["fechaPartido"],horarioPartido=informacion["horarioPartido"])
            partido.save()
            miFormulario=CargaPartido()
            return render(request,"AppTickets/partidos.html",{"miFormulario":miFormulario})
    else:
        miFormulario = CargaPartido()
    return render(request, "AppTickets/partidos.html",{"miFormulario":miFormulario})

@login_required
def clubs(request):
    if request.method == 'POST':
        miFormulario = CargaClub(request.POST,request.FILES)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            try:  ##try-except para evitar fallo al no respetar formato de fecha YYYY-MM-DD
                club = Club(nombreClub=informacion["nombreClub"],nombreEstadio=informacion["nombreEstadio"],direccionEstadio=informacion["direccionEstadio"],capacidadEstadio=informacion["capacidadEstadio"],fechaFundacion=informacion["fechaFundacion"],localidad=informacion["localidad"],provincia=informacion["provincia"],fotoEstadio=informacion["fotoEstadio"],historia=informacion["historia"],timestamp=datetime.now())
                club.save()
            except:
                pass
            miFormulario=CargaClub()
            return render(request,"AppTickets/clubs.html",{"miFormulario":miFormulario})
    else:
        miFormulario = CargaClub()
    return render(request, "AppTickets/clubs.html",{"miFormulario":miFormulario})

@login_required
def buscarSocio(request):
    return render(request, "AppTickets/buscarSocio.html")

@login_required
def buscar(request):
    if request.GET["dni"]:
        dni = request.GET["dni"]
        socios = Socio.objects.filter(dni = dni)
        return render(request,"AppTickets/inicio.html",{"socios":socios})
    else:
        respuesta = "No se enviaron datos"
    
    return render (request, "AppTickets/inicio.html", {"respuesta":respuesta})

@login_required
def leerPartidos(request):
    partidos = Partido.objects.all()
    contexto = {"partidos":partidos}
    return render (request, "AppTickets/ProxPartidos.html",contexto)

@login_required
def listaClubes(request):
    clubes = Club.objects.all()
    contexto = {"clubes":clubes}
    return render (request,"AppTickets/listaClubes.html",contexto)

@login_required
def detalleClub(request,id):
    club = Club.objects.filter(id=id)
    
    if club.exists():
        club = club.first()
        print(club)

    else:
        return HttpResponse("<h1>Pagina no existe </h1>")
    contexto={"club":club}
    print(contexto)
    return render (request, "AppTickets/detalleClub.html",contexto)

@login_required
def eliminarClub(request,id):
    club = Club.objects.get(id= id)
    club.delete()
    clubes = Club.objects.all()
    contexto = {"clubes":clubes}
    return render(request,"AppTickets/listaClubes.html", contexto)

@login_required
def editarClub(request,id):
    club = Club.objects.get(id = id)
    
    if request.method == 'POST':
        miFormulario = CargaClub(request.POST,request.FILES)
        print("paso1")
        if miFormulario.is_valid:
            print(miFormulario)
            print("paso2")
            
            
            data = miFormulario.cleaned_data

            club.nombreClub = data['nombreClub']
            club.nombreEstadio = data['nombreEstadio']
            club.direccionEstadio = data['direccionEstadio']
            club.capacidadEstadio = data['capacidadEstadio']
            try: ##try-except para evitar fallo al no respetar formato de fecha YYYY-MM-DD
                club.fechaFundacion = data['fechaFundacion']
            except:
                pass
            club.localidad = data['localidad']
            club.provincia = data['provincia']
            try: ##try-except para evitar fallo al actualizar informacion del Club sin cargar una nueva foto
                club.fotoEstadio = data['fotoEstadio']
            except:
                pass    
            club.historia = data['historia']
            club.save()
            miFormulario = CargaClub()
            clubes = Club.objects.all()
            contexto = {"clubes":clubes}
            return render(request,"AppTickets/listaClubes.html", contexto)
    else:
        miFormulario = CargaClub(initial={'nombreClub': club.nombreClub, 'nombreEstadio': club.nombreEstadio, 'direccionEstadio': club.direccionEstadio,'capacidadEstadio': club.capacidadEstadio,'fechaFundacion': club.fechaFundacion,'localidad': club.localidad,'provincia': club.provincia,'fotoEstadio': club.fotoEstadio,'historia': club.historia})
        print("paso3")
        return render(request, "AppTickets/editarClub.html", {"miFormulario":miFormulario})


def loginApp(request):
    if request.method == "POST":
        user = authenticate(username = request.POST['user'], password = request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect("../inicio")
        else:
            return render(request, 'AppTickets/login.html', {'error': 'Usuario o contraseña incorrectos'})
    else:
        return render(request, 'AppTickets/login.html')

def registroApp(request):
    if request.method == "POST":
        userCreate = UserCreationForm(request.POST)
        if userCreate is not None:
            try:
                userCreate.save()
                return redirect("../login")
            except:
                return render(request, 'AppTickets/registro.html',{'error': 'Revise los datos Requisitos: Your password cant be too similar to your other personal information. Your password must contain at least 8 characters. Your password cant be a commonly used password. Your password cant be entirely numeric. '})
    else:
        return render(request, 'AppTickets/registro.html')