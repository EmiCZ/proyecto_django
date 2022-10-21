from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Configuracion(models.Model):
    titulo_web = models.CharField(max_length=30)
    nombre_blog = models.CharField(max_length=14)
    construido_por = models.CharField(max_length=30)
    titulo_principal = models.CharField(max_length=30)
    subtitulo = models.CharField(max_length=40)