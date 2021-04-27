def reemplazar(cadena,longMax,costoCorto,costoLargo):       #Separa caracter por caracter, los que exedan el limite los reemplaza y calcula el costo.
    palabras = cadena.split(" ")
    palabras[-1]=palabras[-1].rstrip(".")
    Palabraslargas = 0
    Palabrascortas = 0  
    frase = ""
    for i in range(len(palabras)):
        if len(palabras[i])>longMax:
            frase += palabras[i][0:longMax]+"@" + " "
            Palabraslargas = Palabraslargas + 1

            for letra in palabras[i]:

              if letra == ".":
                  print(palabras[i][-1])
                  frase = f"{frase.strip()}{palabras[i].replace(palabras[i], 'STOP ')}" 
        else:

            frase +=palabras[i]+" "
            Palabrascortas = Palabrascortas + 1

            for letra in palabras[i]:

              if letra == ".":
                  print(palabras[i][-1])
                  frase = f"{palabras[i].replace(palabras[i][-1], 'STOP ')}" 
    
   
    frase = frase.strip() + "STOPSTOP"
    costoT = Palabraslargas*costoL + Palabrascortas*costoC
    return f"El telegrama queda {frase}, y tiene un costo total de {costoT}$ con {Palabraslargas} palabras largas y {Palabrascortas} palabras cortas."

telegrama= input("Ingrese el telegrama: ")

maxLetras= int(input("Ingrese el maximo de letras por palabra: "))

costoC=float(input("Ingrese el costo de las palabras cortas: "))

costoL=float(input("Ingrese el costo de las palabras largas: "))

print(reemplazar(telegrama, maxLetras, costoC, costoL))