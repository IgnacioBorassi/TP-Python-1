#Dado un año, indicar si es bisiesto
def bisiesto(año): 
    if año % 4 != 0: 
	    astronauta = ("No es bisiesto")
    elif año % 4 == 0 and año % 100 != 0: 
	    astronauta = ("Es bisiesto")
    elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0: 
	    astronauta = ("No es bisiesto")
    elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0: 
	    astronauta = ("Es bisiesto")
    return (astronauta)

#Dado un mes, indicar la cantidad de dias
def mes(mes):
    if mes == (str("enero" or "marzo" or "mayo" or "julio" or "agosto" or "octubre" or "diciembre")): 
        print("Tiene 31 dias")
    if mes == (str("Abril" or "junio" or "septiembre" or "noviembre")): 
        print("Tiene 30 dias")
    if mes == (str("Febrero")):
        print("Tiene 28 dias")
    
    return(mes)

#Dada una fecha, indicar si es valida
def fecha(dia, mes, ano):
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
            if bisiesto(ano) == "Es bisiesto":          #Uso la funcion para verificar si el año es bisiesto
                if dia > 0 and dia < 30:                #Las variables t/f las uso para saber si son o no validas las diferentes instancias de la fecha
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

#Dada una fecha, indicar la cantidad de dias faltantes para terminar el mes
def cantidad(dias, mes, ano):
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

def cantidadmeses(dia, mes, ano):               #Todavia esto no funciona
    if fecha(dias, mes, ano) == "Es valido":
        if  bisiesto(ano):     