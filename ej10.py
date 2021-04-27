import random   
from random import randrange
           
random=(random.randrange(30))

intentos = 0
numero = 0

while not numero == random:     #Basicamente compara si es mayor o menor y lo indica, hasta que sea el correcto.
    numero = int(input("Ingrese un numero"))
    
    if numero > random:
        intentos += 1
        print("El numero es menor")

    elif numero < random:
        intentos += 1
        print ("El numero es mayor")
        
    elif numero == random:
        print("Correcto. Intentaste", intentos, "veces")
        intentos = 0
        break