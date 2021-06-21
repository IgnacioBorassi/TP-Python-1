def validar(string):
    cadena = []
    abiertos = "({["
    cerrados = ")}]"

    for i in string:
        if i in abiertos:       #Si el simbolo abierto esta en la cadena, lo mete en otra lista aparte.
            cadena.append(i)
        elif i in cerrados:     #Si el simbolo cerrado esta, y la cadena no tiene otros caracteres, es falso, ya que no tiene que cerrar.
            if len(cadena) == 0:
                return False
            else:               #Pero si hay un sibolo abriendo, hay que fijarse que sea el mismo tipo (parentesis, corchete o llave).   
                simbolo = cadena.pop()      #Guarda el ultimo elemento de la cadena (de simbolos, no el calculo), lo borra y lo pone en la primer posicion, no sin antes guardarlo en una variable para comparar.
                tipoabierto = abiertos[cerrados.index(i)]   #La posicion del cerrado, determina la de abierto. Lo igualo en otra variable para comparar 
                if simbolo != tipoabierto:        #Si son diferentes      
                    return False

    return not len(cadena)


print(validar("1 + 1 ( 1 + 1)"))