# el archivo forms.py puede tener cualquier nombre

from django import forms

class Buscar(forms.Form):
      nombre = forms.CharField(max_length=100)