# Tercera-pre-Entrega-Alcorta
AppTickets
AppTickets es una aplicación para gestionar información relacionada con Socios, Clubes y Partidos. 
Las funcionalidades son: Buscar socios por DNI, cargar nuevos socios, agregar información de clubes y registrar próximos partidos. 

Las secciones principales de la aplicación son:

Inicio (http://127.0.0.1:8000/AppTickets/inicio/)
La sección de inicio incluye un formulario quepermite buscar socios por DNI. Utiliza la vista "Buscar" que realiza un filtrado de los objetos Socio cuyo DNI coincida con el valor recibido a través del método GET.

Socios (http://127.0.0.1:8000/AppTickets/socios/)
En la sección de socios, puedes cargar los datos de nuevos socios. El modelo Socio contiene los campos Nombre, Apellido, DNI y correo. Esta sección hereda de Inicio.html, por lo que también se visualiza la opción de buscar socio. Utiliza el formulario CargaSocio y la vista "socios".

Clubs (http://127.0.0.1:8000/AppTickets/clubs/)
Permite cargar los datos de los clubes. El modelo Club incluye Nombre del club, Estadio, Dirección del estadio y Capacidad del estadio. Esta sección también hereda de Inicio.html y también muestra la opción de buscar socio. Utiliza el formulario CargaClub y la vista clubs.

Partidos (http://127.0.0.1:8000/AppTickets/partidos/)
En esta sección se carga la información de los próximos partidos. El modelo Partido contiene: Equipo Local, Equipo Visitante, Día del partido (en formato YYYY-MM-DD) y Horario (HH:MM). Al igual que en las secciones anteriores, esta sección hereda de Inicio.html y también muestra la opción de buscar socio. Utiliza el formulario CargaPartido y la vista partidos para administrar los datos de los partidos.