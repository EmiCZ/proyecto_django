"""ProyectoDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include #Esto se usa para rutear a otro url.py
from AppCoder.forms import FamiliarForm
from AppCoder.views import saludo
from AppCoder.views import saludo_dos
from AppCoder.views import saludar_a
from AppCoder.views import (mostrar_mi_template, template_con_variables, template_con_listas, mostrar_familiares, BuscarFamiliar, CrearFamiliar,
                             BorrarFamiliar, AltaFamiliar)
from blog.views import index as blog_index

urlpatterns = [
    path('admin/', admin.site.urls),
    path("hola-mundo/saludo/", saludo),
    path("hola-mundo/saludo_2/", saludo_dos),
    path("hola-mundo/saludar/<nombre>/", saludar_a),
    path("template/", mostrar_mi_template),
    path("template2/<nombre>/<apellido>", template_con_variables),
    path("template3/", template_con_listas),
    path("familiares/", mostrar_familiares),
    path("blog/", blog_index),
    path("familiares/buscar", BuscarFamiliar.as_view()),
    path("familiares/crear", CrearFamiliar.as_view()),
    path("familiares/borrar", BorrarFamiliar.as_view()),
    path("familiares/alta", AltaFamiliar.as_view()),
    path("panel-familia/", include('panel_familia.urls')), #en el include pongo el nombre de la aplicación y le agrego .urls
]
