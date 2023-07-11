from django.urls import path
from AppTickets.views import * #inicio,partidos,socios,clubs
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', inicio),
    path('inicio/', inicio),
    path('inicio/', inicio, name="Inicio"),
    path('clubs/', clubs, name="Clubs"),
    path('socios/', socios,name="Socios"),
    path('partidos/', partidos, name="Partidos"),
    path('buscar/', buscar, name="Buscar"),
    path('buscarSocio/', buscarSocio, name="BuscarSocio"),
    path('proxPartidos/', leerPartidos, name="ProxPartidos"),
    path('listaClubes/', listaClubes, name="listaClubes"),
    path('detalleClub/<id>', detalleClub, name="detalleClub"),
    path('eliminarClub/<id>', eliminarClub, name="eliminarClub"),
    path('editarClub/<id>', editarClub, name="editarClub"),
    path('login/', loginApp, name="login"),
    path('registro/', registroApp, name="registro"),
    path('Logout/',LogoutView.as_view(template_name = 'AppTickets/logout.html'), name="Logout"),
    
]

