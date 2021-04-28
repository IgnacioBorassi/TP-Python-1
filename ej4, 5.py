eleccion = int(input("¿Donde desea ingresar? (1, conversor. 2, Diferencia de temperaturas): "))


def conversion(numero):  #Hace la conversion desde la formula.
    farenheit = int (9/5 * numero + 32)
    return (farenheit)


if (eleccion == 1):   #Conversion del numero dado por el usuario.
    numero = int(input("Ingrese un numero a convertir: "))
    print (conversion(numero))


if (eleccion == 2): #El programa pide los datos necesarios para hacer la conversion.
    diferencia = int(input("Ingrese la diferencia enre temperaturas: "))
    minimo = int(input("Ingrese el valor minimo: "))
    maximo = int(input("Inrese el valor maximo: "))
    
    for i in range (minimo, maximo, diferencia):   
        numero = i #Hace la conversion varias veces, haciendo incapie la cantidad de veces que aclaro el usuario. (Fue un castigo esto, no era la consigna)
        print(conversion(numero))

if (eleccion != 1 and eleccion != 2):       #Si la eleccion no es ni 1 ni 2, dice que no es valido.
    print("Ingrese un valor valido")