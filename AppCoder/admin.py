from django.contrib import admin
from AppCoder.models import Familiar #necesito agregar el modelo para usar el admin

# Register your models here.
admin.site.register(Familiar) #Agrego el modelo hay que crear el superuser en el python manage.py