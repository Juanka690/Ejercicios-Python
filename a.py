import re

contraseña = input("Ingrese la contraseña: ")
re = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@!#$%^&*_-]).{8,}.+$')

if re.match(contraseña):
    print("La contraseña es valida")
else:
    print("La contraseña no es valida")

