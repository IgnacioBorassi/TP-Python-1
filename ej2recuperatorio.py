texto = ""

def cantidadpalabras(texto):
    """Devuelve un diccionario con la cantidad de veces que se repitio cada palabra"""
    sacar = [',', '.', ':', ';', '!', '¡', '?', '¿']        
    for i in sacar:
        texto = texto.replace(i, "")            #Saco simbolos que no me interesan para la separacion de las palabras.
    texto = texto.lower()
    palabras = texto.split(" ")                 #Hago una lista por cada palabra del texto dado.
    diccionariopalabras = {}
    for palabra in palabras:
        if palabra in diccionariopalabras:      #Recorro las palabras de la lista y las comparo con las palabras que hay en el diccionario.
            
            diccionariopalabras[palabra] += 1   #Si hay una palabra repetida, sumo uno al 'Value'.
        else:
            diccionariopalabras[palabra] = 1    
    return diccionariopalabras
    
def cantidaddeletras(texto):
    """Devuelve un diccionario con la cantidad de veces que se repitio cada letra"""
    sacar = [',', '.', ':', ';', '!', '¡', '?', '¿']
    for i in sacar:
        texto = texto.replace(i, "")
    texto = texto.lower()
    palabras = texto.split(" ")                
    letra = "".join(palabras)               #Hago un string de la lista de palabras, todas juntas.
    diccionarioletras = {}
    for i in letra:                         #Recorro el string letra por letra.
        if i in diccionarioletras:
            diccionarioletras[i] += 1       #Si hay una letra repetida, sumo uno al 'Value'
        else:
            diccionarioletras[i] = 1
    return diccionarioletras


