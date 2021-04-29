
def calcular(numero1, numero2, numero3, numero4):  
    """Calcula el mayor producto entre todos los numeros dados"""
    mayor = 0 
    producto = numero3 * numero4
    if (producto > mayor):
        mayor = producto

    for i in (numero2, numero3, numero4):
        producto = numero1 * i 
        if (producto > mayor):
            mayor = producto
    for i in (numero3, numero4):
        producto = numero2 * i
        if (producto > mayor):
            mayor = producto
    return(mayor)

def numerosusuario():      
    """Pide numeros al usuario, usa la funcion anterior"""
    resultado = calcularmayorprodutco(int(input("Ingrese un numero: ")),int(input("Ingrese otro numero: ")),int(input("Ingrese otro numero: ")),int(input("Ingrese otro numero: ")))
    print("El mayor producto de todos estos numeros es: ", resultado)

numerosusuario()