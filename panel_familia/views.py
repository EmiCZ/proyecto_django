from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView #Esto es para importar la funcionalidad de CLASS BASED VIEWS basadas en vistas. Ver la clase FamiliarList, FamiliarCrear, FamiliarBorrar, FamiliarActualizar
from AppCoder.models import Familiar #esto es para traerme el modelo desde otra aplicacion. La carpeta "templates" se tiene que llamar igual que la aplicacion donde esta el modelo

class FamiliarList(ListView):
    model = Familiar #Solo tengo que indicar cual es el modelo para generar la lista. Esta lista solo me muestra lo que figura en def __str__(self):

class FamiliarCrear(CreateView):
    model = Familiar #Le indico cual es el modelo sobre el que esto creando
    success_url = "/panel-familia" #Le indico a donde me tiene que llevar en caso de que se cargue correctamente
    fields = ["nombre", "direccion", "numero_pasaporte", "fecha_nacimiento"] #Le indico que campos voy a cargar en el form

class FamiliarBorrar(DeleteView):
    model = Familiar
    success_url = "/panel-familia"

class FamiliarActualizar(UpdateView):
    model = Familiar
    success_url = "/panel-familia"
    fields = ["nombre", "direccion", "numero_pasaporte", "fecha_nacimiento"]
