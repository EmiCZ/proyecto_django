from django.urls import path
from panel_torneo.views import panel_inicial
from panel_torneo.views import (EquiposCrear, EquiposActualizar,EquiposLista,EquiposBuscar,EquiposBorrar)
#separo las urls de la app en su propio archivo urls.py

urlpatterns = [
    path("", panel_inicial, name="inicio"),
    path("lista_equipos", EquiposLista.as_view(), name="equipos-lista"), #le ponemos nombre para poder armar los links
    path("crear_equipos",EquiposCrear.as_view(), name="equipos-crear"),
    path("<int:pk>/borrar_equipos",EquiposBorrar.as_view(), name="equipos-borrar"), #pk es el id del registro de la clase
    path('<int:pk>/actualizar_equipos', EquiposActualizar.as_view(), name="equipos-actualizar"), #pk es el id del registro de la clase
    path("buscar_equipos", EquiposBuscar.as_view(), name="equipos-buscar"),

]