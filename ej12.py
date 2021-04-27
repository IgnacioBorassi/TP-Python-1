cadena = input("ingrese una cadena de caracteres: ")
cont = 0
if cadena == "":
    print("No valido")
else:
    for letra in cadena.upper():
        if letra in "AEIOU":
            cont += 1
    print(cadena, "Tiene ", cont, "vocales")