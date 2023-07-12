from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppTickets.forms import *
from AppTickets.models import *
from datetime import datetime
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

@login_required
def inicio(request):
    avatar = getavatar(request)
    return render(request, "AppTickets/inicio.html",{"avatar":avatar})

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
    avatar = getavatar(request)
    # usuario = request.user
    # print(usuario)
    # user_basic_info = User.objects.get(id = usuario.id)
    # print(user_basic_info)
    # print(user_basic_info.id)
    # print(user_basic_info.username)
    user = User.objects.get(username = request.user)
    if request.method == 'POST':
        miFormulario = CargaClub(request.POST,request.FILES)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            try:  ##try-except para evitar fallo al no respetar formato de fecha YYYY-MM-DD
                club = Club(autorNombre = user.username, nombreClub=informacion["nombreClub"],nombreEstadio=informacion["nombreEstadio"],direccionEstadio=informacion["direccionEstadio"],capacidadEstadio=informacion["capacidadEstadio"],fechaFundacion=informacion["fechaFundacion"],localidad=informacion["localidad"],provincia=informacion["provincia"],fotoEstadio=informacion["fotoEstadio"],historia=informacion["historia"],timestamp=datetime.now())
                print(club)
                club.save()
            except:
                pass
            miFormulario=CargaClub()
            return render(request,"AppTickets/clubs.html",{"miFormulario":miFormulario,"avatar":avatar})
    else:
        miFormulario = CargaClub()
    return render(request, "AppTickets/clubs.html",{"miFormulario":miFormulario,"avatar":avatar})

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
    avatar = getavatar(request)
    partidos = Partido.objects.all()
    contexto = {"partidos":partidos,"avatar":avatar}
    return render (request, "AppTickets/ProxPartidos.html",contexto)

@login_required
def listaClubes(request):
    avatar = getavatar(request)
    clubes = Club.objects.all()
    contexto = {"clubes":clubes,"avatar":avatar}
    return render (request,"AppTickets/listaClubes.html",contexto)

@login_required
def detalleClub(request,id):
    avatar = getavatar(request)
    club = Club.objects.filter(id=id)
    
    if club.exists():
        club = club.first()
        print(club)

    else:
        return HttpResponse("<h1>Pagina no existe </h1>")
    contexto={"club":club,"avatar":avatar}
    print(contexto)
    return render (request, "AppTickets/detalleClub.html",contexto)

@login_required
def eliminarClub(request,id):
    avatar = getavatar(request)
    club = Club.objects.get(id= id)
    club.delete()
    clubes = Club.objects.all()
    contexto = {"clubes":clubes,"avatar":avatar}
    return render(request,"AppTickets/listaClubes.html", contexto)

@login_required
def editarClub(request,id):
    avatar = getavatar(request)
    club = Club.objects.get(id = id)
    user = User.objects.get(username = request.user)
    #user_basic_info = User.objects.get(id = usuario.id)
    
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
            #club.autorid = user
            club.autorNombre = user.username
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
            contexto = {"clubes":clubes,"avatar":avatar}
            return render(request,"AppTickets/listaClubes.html", contexto)
    else:
        miFormulario = CargaClub(initial={'nombreClub': club.nombreClub, 'nombreEstadio': club.nombreEstadio, 'direccionEstadio': club.direccionEstadio,'capacidadEstadio': club.capacidadEstadio,'fechaFundacion': club.fechaFundacion,'localidad': club.localidad,'provincia': club.provincia,'fotoEstadio': club.fotoEstadio,'historia': club.historia})
        print("paso3")
        return render(request, "AppTickets/editarClub.html", {"miFormulario":miFormulario,"avatar":avatar})


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

@login_required
def perfil(request):
    avatar = getavatar(request)


    return render(request,'AppTickets/perfil.html',{"avatar":avatar})


@login_required  
def edicionPerfil(request):
    avatar = getavatar(request)
    usuario = request.user
    user_basic_info = User.objects.get(id = usuario.id)
    if request.method == "POST":
        form = FormEdicionPerfil(request.POST, instance = usuario)
        if form.is_valid():
            user_basic_info.username = form.cleaned_data.get('username')
            user_basic_info.email = form.cleaned_data.get('email')
            user_basic_info.first_name = form.cleaned_data.get('first_name')
            user_basic_info.last_name = form.cleaned_data.get('last_name')
            user_basic_info.save()
            return render(request, 'AppTickets/Perfil.html',{"avatar":avatar})
    else:
        form = FormEdicionPerfil(initial= {'username': usuario.username, 'email': usuario.email, 'first_name': usuario.first_name, 'last_name': usuario.last_name })
        return render(request, 'AppTickets/edicionPerfil.html', {"form": form,"avatar":avatar})

@login_required
def changePassword(request):
    avatar = getavatar(request)
    usuario = request.user    
    if request.method == "POST":
        form = ChangePasswordForm(data = request.POST, user = usuario)
        if form.is_valid():
            if request.POST['new_password1'] == request.POST['new_password2']:
                user = form.save()
                update_session_auth_hash(request, user)
                return render(request, 'AppTickets/Perfil.html',{"avatar":avatar})
        form = ChangePasswordForm(user = usuario)
        return render(request, 'AppTickets/changePassword.html',{"form": form,'error':'Datos incorrectos',"avatar":avatar})
    else:
        form = ChangePasswordForm(user = usuario)
        return render(request, 'AppTickets/changePassword.html', {"form": form,"avatar":avatar})


@login_required
def editAvatar(request): 
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            user = User.objects.get(username = request.user)
            avatar = Avatar(user = user, image = form.cleaned_data['avatar'], linkInfo = form.cleaned_data['linkInfo'] , descripcion = form.cleaned_data['descripcion'], id = request.user.id)
            avatar.save()
            avatar = Avatar.objects.filter(user = request.user.id)
            
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None           
            return render(request, "AppTickets/inicio.html", {'avatar': avatar})
        else:
            user = User.objects.get(username = request.user)
            avatarDummy = Avatar.objects.get(user = user)##obtener imagen actual cuando se quiere actualizar info sin cargar foto nueva
            avatar = Avatar(user = user, image = avatarDummy.image, linkInfo = form.cleaned_data['linkInfo'] , descripcion = form.cleaned_data['descripcion'], id = request.user.id)
            avatar.save()
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None          
            return render(request, "AppTickets/inicio.html", {'avatar': avatar})

    else:
        try:
            print("si funcionó") ##test si entra al try
            user = User.objects.get(username = request.user)
            print(user) ##test si obtiene user
            avatar = Avatar.objects.get(user = user)
            print(avatar.descripcion) ##test si obtiene los objetos
            
            form = AvatarForm(initial= {'avatar':avatar.image,'linkInfo': avatar.linkInfo, 'descripcion': avatar.descripcion})
        except:
            print("no funcionó")
            form = AvatarForm()
        return render(request, "AppTickets/avatar.html", {'form': form})

@login_required
def getavatar(request):
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    return avatar

@login_required
def about(request):
    avatar = getavatar(request)
    return render(request, "AppTickets/about.html",{"avatar":avatar})
