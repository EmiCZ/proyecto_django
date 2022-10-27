from django.db import models

# Create your models here.

class Usuario(models.Model):
    usuario = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    correo = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.usuario}, {self.correo}, {self.id}"

class Torneo(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad_equipos = models.IntegerField()
    region = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre}, {self.cantidad_equipos}, {self.region}, {self.id}"

class Equipos(models.Model):
    nombre = models.CharField(max_length=100)
    torneo = models.CharField(max_length=100)
    cantidad_jugadores = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre}, {self.torneo}, {self.cantidad_jugadores}, {self.id}"

class Jugadores(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    equipo = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    

    def __str__(self):
        return f"{self.nombre}, {self.apellido}, {self.equipo}, {self.fecha_nacimiento}, {self.id}"

class Partidos(models.Model):
    equipo_local = models.CharField(max_length=100)
    equipo_visitante = models.CharField(max_length=100)
    goles_local = models.IntegerField()
    goles_visitante = models.IntegerField()
    

    def __str__(self):
        return f"{self.equipo_local}, {self.goles_local}, {self.equipo_visitante}, {self.goles_visitante}, {self.id}"
