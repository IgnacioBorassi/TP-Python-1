palabra = input("Ingrese una palabra: ")
palabra2 = input("Ingrese otra palabra: ")

def verificar(palabra,palabra2):  #Verifica que la primer palabra, es igual que la segunda en mayusculas
    if palabra == palabra2.upper():
        return True
    else: 
        return False
        
if verificar(palabra,palabra2):
    print("La palabra", palabra, "es la version capitalizada de", palabra2)
else:
    print("La palabra", palabra, "no es la version capitalizada de", palabra2)