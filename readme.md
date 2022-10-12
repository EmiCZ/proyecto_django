#Clase 17

Django es un framework que nos permite crear aplicaciones web, es uno de los mas completos

Hay otros frameworks que cubren otras necesidades:
    - Dash sirve para el analisis de datos
    - Flask es un framework minimalista que es necesario personalizar para poder utilizar al maximo

Django trabajo con el modelo de MVT (Model, View, Template)

https://masteringdjango.com/ #Información sobre como utilizar Django

View es donde esta la logica de como procesar la información y que tareas se deben realizar dependiendo del input del cliente
Template es donde esta la logica para definir como le muestro esa información que proceso en "View"
Model es donde se guarda la información en la base de datos

Para instalar Django uso pip install Django

Django utiliza el concepto de proyecto. 
Hay que usar el siguiente comando para crear el proyecto: django-admin startproject NombreDeProyecto . (en el directorio del proyecto de VSC)
Con el . hago que no me genere la carpeta superior y me genera directamente todo en la carpeta principal

Al iniciar el proyecto debemos usar este comando en la terminal python manage.py migrate (en el directorio del proyecto de VSC) para generar la base de datos "db.sqlite3" para poder administrar

Para verificar que esto se hizo correctamente corremos el comando python manage.py runserver (en el directorio del proyecto de VSC) e ingresamos en el browse la direccion donde dice "Starting development server at xxxxx" para ver la imagin donde dice que se instalo correctamente
Para frenar el servidor usamos CTRL + C

Los proyectos de Django puede incluir muchas aplicaciones (Apps) que cada una resuelve problemas de forma independiente
Para crear aplicaciones corremos el comando python manage.py startapp (en el directorio del proyecto de VSC)