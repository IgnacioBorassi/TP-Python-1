def perimetro(altura, base):
    """Dada la altura y la base de un rectangulo, calcular el perimetro"""
    return (altura*2 + base*2)

def area(altura, base):
    """Dada la altura y la base de un rectangulo, calcular su area"""
    return (altura*base)

def circulo(radio):
    "Dado el radio de un circulo calcular el perimetro"
    return (2*3.14*(radio*radio))

def acirculo(radio):
    "Dado el radio de un circulo calcular el area"
    return (3.14*(radio*radio))

def esfera(radio):
    """Dado el radio de una esfera, calcular su volumen"""
    return ((4/3*3.14*radio))

def hipotenusa(lado1, lado2):
    """Dado los catetos de un triangulo isoceles, calcular su hipotenusa"""
    return ((lado1*lado1)+(lado2*lado2))
