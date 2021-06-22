romanos = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]

def conversoraromano(entero): 
    """Convierte el numero entero en romano"""
    resultado = ""
    while entero > 0:
        for n, r in romanos:
            while entero > n or entero == n:
                resultado = resultado + r
                entero = entero - n
    return resultado

entero = int(input("Ingrese un numero entero: "))
if entero < 0:                     #Checker si es valido o no
    "Ingreso un numero entero no valido"
elif entero == 0:
    "No se puede representar el 0 en la numerologia romana"
else: 
    print(conversoraromano(entero)) 

