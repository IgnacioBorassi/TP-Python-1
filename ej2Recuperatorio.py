import random
from random import randrange
tiradas = int(input("Ingrese cantidad de tiradas: "))
def dados(tiradas):
    uno = 0
    dos = 0
    tres = 0
    cuatro = 0
    cinco = 0
    seis = 0
    for i in range(tiradas * 2):
        random = randrange(1,6)
        if random == 1:
            uno = uno + 1
        if random == 2:
            dos = dos + 1 
        if random == 3:
            tres = tres + 1
        if random == 4:
            cuatro = cuatro + 1
        if random == 5:
            cinco = cinco + 1  
        if random == 6: 
            seis = seis + 1   
    if uno != 0:
        print("El numero 1 salio: ", uno, "veces")
    if dos != 0:
        print("El numero 2 salio: ", dos, "veces")
    if tres != 0:
        print("El numero 3 salio: ", tres, "veces")
    if cuatro != 0:
        print("El numero 4 salio: ", cuatro, "veces")
    if cinco != 0:
        print("El numero 5 salio: ", cinco, "veces")
    if seis != 0:
        print("El numero 6 salio: ", seis, "veces")
    return tiradas
    
print(dados(tiradas))