def validar(calculo):
    """Valida una cadena de calculos matematicos para saber si los simbolos como corchetes, parentesis y llaves, estan bien colocados"""
    cadena = []
    abiertos = "({["
    cerrados = ")}]"

    for i in calculo:
        if i in abiertos:       #Si el simbolo abierto esta en la cadena, lo mete en otra lista aparte.
            cadena.append(i)
        elif i in cerrados:     #Si el simbolo cerrado esta, y la cadena no tiene otros caracteres, es falso, ya que no tiene qué cerrar.
            if len(cadena) == 0:
                return False
            else:               #Pero si hay un sibolo abriendo, verifica que sea el mismo tipo (parentesis, corchete o llave).   
                simbolo = cadena.pop()    
                tipoabierto = abiertos[cerrados.index(i)]   #La posicion del cerrado, determina la de abierto. Lo igualo en otra variable para comparar 
                if simbolo != tipoabierto:        #Si son diferentes, el simbolo de cierre es diferente al de apertura, por lo tanto: False     
                    return False

    return not len(cadena)