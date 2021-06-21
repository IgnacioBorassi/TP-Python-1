letras = ['1', '2', '3', '4', '5','6', '7', '8', '9','0', '.', ',',' ','a','b','c','d','e','f','g','h','i','j',
          'k','l','m','n','o','p','q','r','s','t',
          'u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J',
          'K','L','M','N','O','P','Q','R','S','T',
          'U','V','W','X','Y','Z']
rot13= ['1', '2', '3', '4', '5','6', '7', '8', '9','0','.', ',',' ','n','o','p','q','r','s','t',
        'u','v','w','x','y','z','a','b','c','d',
        'e','f','g','h','i','j',
        'k','l','m','N','O','P','Q','R','S','T',
        'U','V','W','X','Y','Z','A','B','C','D',
        'E','F','G','H','I','J',
        'K','L','M']

def transformacionrot13(frase):
    """Encripta con ROT13 una cadena de texto que le entregues"""
    longitud = len(frase)                      #Determino la cantidad de veces que voy a recorrer la lista de letras para comparar (cantidad de letras)
    frase = frase.lower()
    conversion = ""
    for i in range(0, longitud):
            for x in range (0, 39):
                if frase[i] == letras[x]:      #Comparo los caracteres con todos los de la lista de letras, el que es igual, lo reemplazo por la misma posicion en la ROT13 
                    conversion += rot13[x]          
    return conversion