from django.urls import path
from panel_torneo.views import UsuarioActualizar, UsuarioBuscar, UsuarioCrear, UsuarioLista, panel_inicial
from panel_torneo.views import (EquiposCrear,EquiposActualizar,EquiposLista,EquiposBuscar,EquiposBorrar,
                                UsuarioCrear,UsuarioActualizar,UsuarioLista,UsuarioBuscar,UsuarioBorrar,
                                JugadoresCrear, JugadoresActualizar, JugadoresLista, JugadoresBorrar,
                                PartidosCrear, PartidosActualizar, PartidosLista, PartidosBorrar,
                                TorneoCrear, TorneoActualizar, TorneoLista, TorneoBorrar,
                                )
#separo las urls de la app en su propio archivo urls.py

urlpatterns = [
    path("", panel_inicial, name="inicio"),
    path("lista_equipos", EquiposLista.as_view(), name="equipos-lista"),
    path("crear_equipos",EquiposCrear.as_view(), name="equipos-crear"),
    path("<int:pk>/borrar_equipos",EquiposBorrar.as_view(), name="equipos-borrar"), #pk es el id del registro de la clase
    path('<int:pk>/actualizar_equipos', EquiposActualizar.as_view(), name="equipos-actualizar"), #pk es el id del registro de la clase
    path("buscar_equipos", EquiposBuscar.as_view(), name="equipos-buscar"),
    path("lista_jugadores", JugadoresLista.as_view(), name="jugadores-lista"),
    path("crear_jugadores",JugadoresCrear.as_view(), name="jugadores-crear"),
    path("<int:pk>/borrar_jugadores",JugadoresBorrar.as_view(), name="jugadores-borrar"), #pk es el id del registro de la clase
    path('<int:pk>/actualizar_jugadores', JugadoresActualizar.as_view(), name="jugadores-actualizar"), #pk es el id del registro de la clase
    path("lista_partidos", PartidosLista.as_view(), name="partidos-lista"),
    path("crear_partidos",PartidosCrear.as_view(), name="partidos-crear"),
    path("<int:pk>/borrar_partidos",PartidosBorrar.as_view(), name="partidos-borrar"), #pk es el id del registro de la clase
    path('<int:pk>/actualizar_partidos', PartidosActualizar.as_view(), name="partidos-actualizar"), #pk es el id del registro de la clase
    path("lista_torneo", TorneoLista.as_view(), name="torneo-lista"),
    path("crear_torneo",TorneoCrear.as_view(), name="torneo-crear"),
    path("<int:pk>/borrar_torneo",TorneoBorrar.as_view(), name="torneo-borrar"), #pk es el id del registro de la clase
    path('<int:pk>/actualizar_torneo', TorneoActualizar.as_view(), name="torneo-actualizar"), #pk es el id del registro de la clase
    path("lista_usuario", UsuarioLista.as_view(), name="usuario-lista"),
    path("crear_usuario",UsuarioCrear.as_view(), name="usuario-crear"),
    path("<int:pk>/borrar_usuario",UsuarioBorrar.as_view(), name="usuario-borrar"), #pk es el id del registro de la clase
    path('<int:pk>/actualizar_usuario', UsuarioActualizar.as_view(), name="usuario-actualizar"), #pk es el id del registro de la clase
    path("buscar_usuario", UsuarioBuscar.as_view(), name="usuario-buscar"),
    
]