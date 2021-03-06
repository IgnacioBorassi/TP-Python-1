#Dado un ano, indicar si es bisiesto
def bisiesto(ano): 
    if ano % 4 != 0: 
	    respuesta = ("No es bisiesto")
    elif ano % 4 == 0 and ano % 100 != 0: 
	    respuesta = ("Es bisiesto")
    elif ano % 4 == 0 and ano % 100 == 0 and ano % 400 != 0: 
	    respuesta = ("No es bisiesto")
    elif ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0: 
	    respuesta = ("Es bisiesto")
    return (respuesta)

#Dado un mes, indicar la cantidad de dias
def cantidaddiames(mes):
    if mes == (int(1 or 3 or 5 or 7 or 8 or 10 or 12)): 
        cantdias = 31
    if mes == (int(4 or 6 or 9 or 11)): 
        cantdias = 30
    if mes == (int(2)):
        cantdias = 28
    
    return(cantdias)

#Dada una fecha, indicar si es valida
def fechavalida(dia, mes, ano):
    if ano >= 0: 
        resultadoano = True
    else: 
        resultadoano = False
    if mes > 0 and mes < 13:  
        if mes in [1, 3, 5, 7, 8, 10, 12]:
            if dia > 0 and dia < 32:
                resultadodia = True
            else: 
                resultadodia = False
        elif mes == 2:
            if bisiesto(ano) == "Es bisiesto":          #Uso la funcion para verificar si el ano es bisiesto.
                if dia > 0 and dia < 30:                #Las variables t/f las uso para saber si son o no validas las diferentes instancias de la fecha.
                    resultadodia = True
                else: 
                    resultadodia = False   
            else: 
                if dia > 0 and dia < 29:
                    resultadodia = True
                else: 
                    resultadodia = False   
        else:
            if dia > 0 and dia < 31:
                resultadodia = True
            else: 
                resultadodia = False
    else: 
        resultadodia= False
    if resultadodia == True and resultadoano == True:
        validacion = "Es valido"
    else:
        validacion = "No es valido"
    return(validacion)

#Dada una fecha, indicar la cantidad de dias faltantes para terminar el mes.
def cantidaddediasfindemes(dias, mes, ano):
    if fecha(dias, mes, ano) == "Es valido":
        if bisiesto(ano) == "Es bisiesto" and mes == 2:
            diasfaltantes = 29 - dias
            return(diasfaltantes)
        if mes in [1, 3, 5, 7, 8, 10, 12]:
            diasfaltantes = 31 - dias
            return(diasfaltantes)
        else:
            diasfaltantes = 30 - dias
            return(diasfaltantes)
    else: 
        print("No es valido") 

def findeano(dia, mes, ano):                #Calcula la cantidad de dias que faltan para terminar el ano.
    if (fecha(dia, mes, ano)) == "Es valido":
        dias = cantidaddediasfindemes(dia, mes, ano)
        for i in range(mes, 12):
            dias += mes(i)
        return dias
    else:
        return "La fecha no es valida"

        