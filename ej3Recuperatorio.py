def dados(tiradas):
    """Tira dos dados a la azar y cuenta la cantidad de veces que sale cierto resultado""" 
    import random
    resultados = []
    for i in range(tiradas):
        sumadados = random.randint(1, 6) + random.randint(1, 6)     #Al haber dos dados, dos randoms.
        resultados.append(sumadados)
        diccionariosumas = {}
        for sumadados in resultados:
            if sumadados in diccionariosumas:      #Recorro los resultados de la lista y las comparo con los resultados que hay en el diccionario.
                diccionariosumas[sumadados] += 1   #Si hay un resultado repetido, sumo uno al 'Value'.
            else:
                diccionariosumas[sumadados] = 1    
    return diccionariosumas
