def invertirlistaauxiliar(cadena):          #Convierte "Cadena" en una lista aparte y la invierte
  lista = cadena.split(" ")
  lista2 = []
  longitud = len(lista)
  
  for i in range(longitud):
    lista2.append(lista[longitud-i-1])
  
  return " ".join(lista2)

def invertirLista(cadena):                 #Convierte "Cadena" en 1/"Cadena" en si misma, eliminando las palabras y luego volviendolas a añadir
  lista = cadena.split(" ")
  longitud = len(lista)
  
  for i in range(longitud):
      lista.append(lista[longitud-i-1])
      lista.remove(lista[longitud-i-1])
  
  return " ".join(lista)

cadena = input("Ingese una cadena a invertir: ")
print(invertirlistaauxiliar(cadena))
print(invertirLista(cadena))