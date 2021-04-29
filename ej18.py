def invertirlistaauxiliar(cadena):          
  """Convierte la cadena en una lista aparte y la invierte"""
  lista = cadena.split(" ")
  lista2 = []
  longitud = len(lista)
  
  for i in range(longitud):
    lista2.append(lista[longitud-i-1])
  
  return " ".join(lista2)

def invertirLista(cadena):                 
  """Invierte una cadena en si misma, eliminando las palabras y volviendolas a anadir"""
  lista = cadena.split(" ")
  longitud = len(lista)
  
  for i in range(longitud):
      lista.append(lista[longitud-i-1])
      lista.remove(lista[longitud-i-1])
  
  return " ".join(lista)

cadena = input("Ingese una cadena a invertir: ")
print(invertirlistaauxiliar(cadena))
print(invertirLista(cadena))