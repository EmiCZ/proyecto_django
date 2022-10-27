from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView #Esto es para importar la funcionalidad de CLASS BASED VIEWS basadas en vistas. Ver la clase FamiliarList, FamiliarCrear, FamiliarBorrar, FamiliarActualizar
from panel_torneo.models import Usuario, Torneo, Equipos, Jugadores, Partidos
from panel_torneo.forms import Buscar

#Panel Inicial

def panel_inicial(request):
    return render(request,"panel_torneo/panel_torneo.html")

#CRUD Usuario + Busqueda

class UsuarioLista(ListView):
    model = Usuario

class UsuarioCrear(CreateView):
    model = Usuario
    success_url = "/panel-torneo/lista_usuario"
    fields = ["usuario", "password", "correo"]

class UsuarioBorrar(DeleteView):
    model = Usuario
    success_url = "/panel-torneo/lista_usuario"

class UsuarioActualizar(UpdateView):
    model = Usuario
    success_url = "/panel-torneo/lista_usuario"
    fields = ["usuario", "password", "correo"]

class UsuarioBuscar(View):

    form_class = Buscar
    template_name = 'panel_torneo/usuario_buscar.html'
    initial = {"nombre":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            usuarios = form.cleaned_data.get("nombre")
            lista_usuarios = Usuario.objects.filter(usuario__icontains=usuarios).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_usuarios':lista_usuarios})

        return render(request, self.template_name, {"form": form})

#CRUD Torneo

class TorneoLista(ListView):
    model = Torneo

class TorneoCrear(CreateView):
    model = Torneo
    success_url = "/panel-torneo/lista_torneo"
    fields = ["nombre", "cantidad_equipos", "region"]

class TorneoBorrar(DeleteView):
    model = Torneo
    success_url = "/panel-torneo/lista_torneo"

class TorneoActualizar(UpdateView):
    model = Torneo
    success_url = "/panel-familia/lista_torneo"
    fields = ["nombre", "cantidad_equipos", "region"]

#CRUD Equipos + Busqueda

class EquiposLista(ListView):
    model = Equipos

class EquiposCrear(CreateView):
    model = Equipos
    success_url = "/panel-torneo/lista_equipos"
    fields = ["nombre", "torneo", "cantidad_jugadores"]

class EquiposBorrar(DeleteView):
    model = Equipos
    success_url = "/panel-torneo/lista_equipos"

class EquiposActualizar(UpdateView):
    model = Equipos
    success_url = "/panel-torneo/lista_equipos"
    fields = ["nombre", "torneo", "cantidad_jugadores"]

class EquiposBuscar(View):

    form_class = Buscar
    template_name = 'panel_torneo/equipo_buscar.html'
    initial = {"nombre":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_equipos = Equipos.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_equipos':lista_equipos})

        return render(request, self.template_name, {"form": form})

#CRUD Jugadores

class JugadoresLista(ListView):
    model = Jugadores

class JugadoresCrear(CreateView):
    model = Jugadores
    success_url = "/panel-torneo/lista_jugadores"
    fields = ["nombre", "apellido", "equipo", "fecha_nacimiento"]

class JugadoresBorrar(DeleteView):
    model = Jugadores
    success_url = "/panel-torneo/lista_jugadores"

class JugadoresActualizar(UpdateView):
    model = Jugadores
    success_url = "/panel-familia/lista_jugadores"
    fields = ["nombre", "apellido", "equipo", "fecha_nacimiento"]

#CRUD Partidos

class PartidosLista(ListView):
    model = Partidos

class PartidosCrear(CreateView):
    model = Partidos
    success_url = "/panel-torneo/lista_partidos"
    fields = ["equipo_local", "goles_local", "equipo_visitante", "goles_visitante"]

class PartidosBorrar(DeleteView):
    model = Partidos
    success_url = "/panel-torneo/lista_partidos"

class PartidosActualizar(UpdateView):
    model = Partidos
    success_url = "/panel-familia/lista_partidos"
    fields = ["equipo_local", "goles_local", "equipo_visitante", "goles_visitante"]

