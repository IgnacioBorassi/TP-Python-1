eleccion = int(input("¿Donde desea ingresar? (1, conversor. 2, Diferencia de temperaturas): "))


def conversion(numero):
    farenheit = int (9/5 * numero + 32)
    return (farenheit)


if (eleccion == 1):
    numero = int(input("Ingrese un numero a convertir: "))
    print (conversion(numero))


if (eleccion == 2):
    diferencia = int(input("Ingrese la diferencia enre temperaturas: "))
    minimo = int(input("Ingrese el valor minimo: "))
    maximo = int(input("Inrese el valor maximo: "))
    for i in range (minimo, maximo, diferencia):
        numero = i
        print(conversion(numero))

if (eleccion != 1 and eleccion != 2):
    print("Ingrese un valor valido")