def reemplazar(cadena,longMax,costoCorto,costoLargo):   
    """Determina las palabras largas, arregla el exediente y reemplaza STOP en los puntos y STOP STOP en el fin""" 
    palabras = cadena.split(" ")
    palabras[-1]=palabras[-1].rstrip(".")
    Palabraslargas = 0
    Palabrascortas = 0  
    frase = ""
    for i in range(len(palabras)):  
        if len(palabras[i]) > longMax:              #Determina si las palabras se consideran largas o no.

            frase += palabras[i][0:longMax] + "@" + " " #Las palabras que se excedan del largo, se les agrega un '@' en vez de lo sobrante.

            Palabraslargas = Palabraslargas + 1     #Suma al contador de palabras largas.

            for letra in palabras[i]:

              if letra == ".":          #Si hay un punto, convierte ese punto por la palabra STOP.
                  print(palabras[i][-1])
                  frase = f"{frase.strip()}{palabras[i].replace(palabras[i], 'STOP ')}" 
        else:

            frase += palabras[i]+" "  #Si no son palabras consideradas largas, son cortas.
            Palabrascortas = Palabrascortas + 1
            
            for letra in palabras[i]:
                   
                if letra == ".":
                  print(palabras[i][-1])
                  frase = f"{frase.strip()}{palabras[i].replace(palabras[i], 'STOP ')}" 
   
    frase = frase.strip() + "STOPSTOP"
    costoT = Palabraslargas * costoL + Palabrascortas * costoC
    return f"El telegrama queda {frase}, y tiene un costo total de {costoT}$ con {Palabraslargas} palabras largas y {Palabrascortas} palabras cortas."

telegrama= input("Ingrese el telegrama: ")

maxLetras= int(input("Ingrese el maximo de letras por palabra: "))

costoC=float(input("Ingrese el costo de las palabras cortas: "))                     #Pido los datos del usuario

costoL=float(input("Ingrese el costo de las palabras largas: "))

print(controladordetelegramas(telegrama, maxLetras, costoC, costoL))