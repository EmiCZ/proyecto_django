from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Familiar

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

def mostrar_familiares(request):
    lista_familiares = Familiar.objects.all()
    return render(request, "AppCoder/familiares.html", 
                {"lista_familiares" : lista_familiares}) #este diccionario se llama "contexto"