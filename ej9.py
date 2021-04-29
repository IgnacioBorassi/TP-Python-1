import time
from time import sleep

contrasena = "estoesunacontraseñainventada" #Contrasena muy dificil inadivinable
fallos = 3
pausas = 2

while fallos > 0: 
    contrasenausuario = (input("Ingrese la contraseña: "))
    if contrasena == contrasenausuario:
        print("La contraseña ingresada es correcta")
        break                                                   #Si es correcta, finalizar el programa
    else:
        print("Contraseña incorrecta")
        fallos -= 1
        if (fallos == 0):
            print("Demasiados intentos, ingrese mas tarde")

        else: 
            print("A usted le quedan: ", fallos, "Intento(s)")
            time.sleep(pausas)
            pausas += 1
