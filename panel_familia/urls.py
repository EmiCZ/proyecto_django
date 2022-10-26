from django.urls import path
from panel_familia.views import (FamiliarList,FamiliarCrear, FamiliarBorrar, FamiliarActualizar)
#separo las urls de la app en su propio archivo urls.py

urlpatterns = [
    path("", FamiliarList.as_view(), name="familiar-lista"), #le ponemos nombre para poder armar los links
    path("crear",FamiliarCrear.as_view(), name="familiar-crear"),
    path("<int:pk>/borrar",FamiliarBorrar.as_view(), name="familiar-borrar"), #pk es el id del registro de la clase
    path('<int:pk>/actualizar', FamiliarActualizar.as_view(), name="familiar-actualizar"), #pk es el id del registro de la clase
]