from AppCoder.models import Familiar

Familiar(nombre="Luciano", direccion="Bonifacio 801", numero_pasaporte=35999999).save()
Familiar(nombre="Yamila", direccion="Belgrano 1930", numero_pasaporte=35888888).save()
Familiar(nombre="Ricardo", direccion="Cordoba 3545", numero_pasaporte=13999999).save()
Familiar(nombre="Carmen", direccion="Gaona 2539", numero_pasaporte=14999999).save()

print("Se cargo con éxito los usuarios de pruebas")