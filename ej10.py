import random   
from random import randrange
           
random=(random.randrange(50))

intentos = 0
numero = 0

while not numero == random:
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