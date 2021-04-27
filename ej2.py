def perimetro(h, b):
    "Dada la altura y la base de un rectangulo, calcular el perimetro"
    return (h*2 + b*2) #Podria ser (2h + 2b)

def area(h, b):
    "Dada la altura y la base de un rectangulo, calcular su area"
    return (h*b)

def circulo(r):
    "Dado el radio de un circulo calcular el perimetro"
    return (2*3.14*(r*r))

def acirculo(r):
    "Dado el radio de un circulo calcular el area"
    return (3.14*(r*r))

def esfera(r):
    "Dado el radio de una esfera, calcular su volumen"
    return ((4/3*3.14*r))

def hipotenusa(l1, l2):
    "Dado los catetos de un triangulo isoceles, calcular su hipotenusa"
    return ((l1*l1)+(l2*l2))
