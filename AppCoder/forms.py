# el archivo forms.py puede tener cualquier nombre

from django import forms

class Buscar(forms.Form):
      nombre = forms.CharField(max_length=100)

class Crear(forms.Form):
      nombre = forms.CharField(max_length=100)
      direccion = forms.CharField(max_length=200)
      numero_pasaporte = forms.IntegerField()

class Borrar(forms.Form):
      id = forms.IntegerField()