def siglas(oracion):                #Devuelve la primer letra de las palabras de la oracion en forma de siglas.
    palabras = oracion.split(" ")
    resultado = ""

    for palabra in palabras:
        resultado += palabra[0]

    return resultado.upper()

def mayuscula(oracion):                         #Convierte a mayusculas la primer letra de cada palabra de la oracion.
    palabras = oracion.split(" ")

    resultado = ""

    for palabra in palabras:

        resultado += palabra.capitalize() + " "

    return resultado

def palabrascona(oracion):                  #Solo muestra las palabras que comiencen con A.
    palabras = oracion.split(" ")

    resultado = ""

    for palabra in palabras:

        if palabra[0] == "a" or palabra[0] == "A":
            resultado += palabra + " "

    if resultado == "":

        resultado = "No se ingresaron palabras con A"

    return resultado


print(siglas("Fideos enigmaticos de estocolmo"))        #Esto no es un soborno
