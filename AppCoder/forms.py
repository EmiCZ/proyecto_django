# el archivo forms.py puede tener cualquier nombre

from django import forms
from AppCoder.models import Familiar

class Buscar(forms.Form):
      nombre = forms.CharField(max_length=100)

class Crear(forms.Form): #Este fue creado por mi
      nombre = forms.CharField(max_length=100)
      direccion = forms.CharField(max_length=200)
      numero_pasaporte = forms.IntegerField()

class Borrar(forms.Form):
      id = forms.IntegerField()


class Buscar(forms.Form):
  nombre = forms.CharField(max_length=100)

class FamiliarForm(forms.ModelForm): #Este es el ejemplo del profesor
  class Meta: #esta clase ya viene con el framework
    model = Familiar #este es el modelo con el que queremos vincular el formulario. Hay que hacer un import
    fields = ['nombre', 'direccion', 'numero_pasaporte', 'fecha_nacimiento'] #tenemos que definir que campos vamos a usar en el modelo