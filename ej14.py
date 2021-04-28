import random

random = str(random.randrange(1000, 9999))
resultado = ""
aciertos = 0

for numero in random:
    while numero in resultado:
        numero = str(random.randrange(0, 9))
    resultado = resultado + numero
while True:
    coincidencia = 0
    aciertos = 0
    try:
        adivinar= int(input("Intenta adivinar: "))
        if adivinar > 1000:         
            adivinar = str(adivinar)
            for numero in random:
                if numero in str(adivinar):             
                    coincidencia = coincidencia + 1

            for i in range(1,5):
                    if(adivinar[i-1:i] == resultado[i-1:i]):
                        aciertos +=1
            
            coincidencia = coincidencia - aciertos
            
            if int(adivinar) != int(resultado):
                print("tuviste", coincidecia, "coincidencias y", aciertos, "aciertos")

            elif  int(adivinar) == int(resultado):
                print("Felicidades. Ganaste")
            break
        else:
            print("No puede empezar por cero, ni ser negativo. Posee 4 digitos")
    except:
        print("Codigo invalido")
        
