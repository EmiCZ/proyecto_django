from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Familiar
from AppCoder.forms import Buscar, FamiliarForm # <--- Esto es para CLASS BASED VIEWS
from AppCoder.forms import Crear # <--- Esto es para CLASS BASED VIEWS (Creada por mi)
from AppCoder.forms import Borrar # <--- Esto es para CLASS BASED VIEWS (Creada por mi)
from django.views import View # <-- Esto es para CLASS BASED VIEWS


# Create your views here.

def saludo(request): #consulta o petición
    return HttpResponse("Hola Mi Primer App") #respuesta

def saludo_dos(request):
    return HttpResponse("Este es otro saludo")

def saludar_a(request, nombre):
    return HttpResponse(f"Hola como estas {nombre}")

def mostrar_mi_template(request):
    return render(request,"AppCoder/index.html", {
        "nombre":"Yami",
        "apellido" : "Rodriguez"
        })
    
def template_con_variables(request, nombre, apellido):
    return render(request,"AppCoder/index.html", {
        "nombre":nombre,
        "apellido" : apellido
        })

def template_con_listas(request):
    return render(request,"AppCoder/index.html", 
    {"notas": [1,2,3,4,5,6,7,8]}
    )

def mostrar_familiares(request): #esto es una function based view
    lista_familiares = Familiar.objects.all()
    return render(request, "AppCoder/familiares.html", 
                {"lista_familiares" : lista_familiares}) #este diccionario se llama "contexto"

class BuscarFamiliar(View):

    form_class = Buscar
    template_name = 'AppCoder/buscar.html'
    initial = {"nombre":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form}) #Esta variable FORM es la que esta en el codigo del HTML

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_familiares':lista_familiares})

        return render(request, self.template_name, {"form": form})

class CrearFamiliar(View):

    form_class = Crear
    template_name = 'AppCoder/crear.html'
    initial = {"nombre":"", "direccion":"","numero_pasaporte":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form}) #Esta variable FORM es la que esta en el codigo del HTML

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre_form = form.cleaned_data.get("nombre")
            direccion_form = form.cleaned_data.get("direccion")
            numero_pasaporte_form = form.cleaned_data.get("numero_pasaporte")
            Familiar(nombre = nombre_form, direccion = direccion_form, numero_pasaporte = numero_pasaporte_form).save()
            lista_familiares = Familiar.objects.all() 
            #form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_familiares':lista_familiares})

        return render(request, self.template_name, {"form": form})

class BorrarFamiliar(View):

    form_class = Borrar
    template_name = 'AppCoder/borrar.html'
    initial = {"id":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        lista_familiares = Familiar.objects.all()
        return render(request, self.template_name, {'form':form, 'lista_familiares':lista_familiares}) #Esta variable FORM es la que esta en el codigo del HTML

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            id_form = form.cleaned_data.get("id")
            Familiar(id = id_form).delete()
            lista_familiares = Familiar.objects.all()
            return render(request, self.template_name, {'form':form, 
                                                        'lista_familiares':lista_familiares})

        return render(request, self.template_name, {"form": form})

class AltaFamiliar(View):

    form_class = FamiliarForm
    template_name = 'AppCoder/alta_familiar.html'
    initial = {"nombre":"", "direccion":"", "numero_pasaporte":"", "fecha_nacimiento":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el familiar {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})

