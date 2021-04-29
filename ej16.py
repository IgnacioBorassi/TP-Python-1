def consonantes(palabra):       
    """Solo muestra las consonantes de las palabras.""" 
    resultado = ""
    for i in palabra:
        if not i in "aeiouAEIOU":
            resultado += i
    return resultado



def vocales(palabra):        
    """Solo muestra las vocales de las palabras."""
    resultado = ""
    for i in palabra:
        if i in "aeiouAEIOU":
            resultado += i
    return resultado


def moverVocales(palabra):              
    """"Cambia una vocal por la siguiente en la lista."""
    vocales = ["a", "e", "i", "o", "u"]
    for letra in palabra:
        if letra in "aeiouAEIOU":
            for i in range (0,4):
                if letra == vocales[i]:
                    palabra = palabra.replace(letra,vocales[i+1])
            if(letra == "u"):
                palabra = palabra.replace(letra, vocales[0])
    return palabra

def capicua(palabra):              
    """Devuelve true or false si es o no capicua"""
    if palabra == palabra[::-1]:
        return "True"
    else: 
        return "False"