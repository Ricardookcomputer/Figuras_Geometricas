
#######Escribir una clase en python llamada círculo que contenga un radio, con un método que devuelva el área y otro que devuelva el perímetro del círculo


import math

def calcular_circulo(radio):
    # Fórmulas para calcular el perímetro y el área
    perimetro = 2 * math.pi * radio
    area = math.pi * radio ** 2
    
    return perimetro, area

# Solicitar el radio al usuario
radio = float(input("Ingresa el valor del radio: "))

# Llamar a la función para obtener el perímetro y el área
perimetro, area = calcular_circulo(radio)

# Mostrar los resultados
print(f"El perímetro del círculo es: {perimetro:.2f}")
print(f"El área del círculo es: {area:.2f}")

####Escribir una clase en python llamada rectángulo que contenga una base y una altura, y que contenga un método que devuelva el área del rectángulo

class Rectangulo:
    def __init__(self, base, altura):
        # Constructor que inicializa base y altura
        self.base = base
        self.altura = altura

    def calcular_area(self):
        # Método que calcula el área del rectángulo
        return self.base * self.altura

# Solicitar la base y la altura al usuario
base = float(input("Ingresa la base del rectángulo: "))
altura = float(input("Ingresa la altura del rectángulo: "))

# Crear un objeto de la clase Rectangulo
rectangulo = Rectangulo(base, altura)

# Calcular y mostrar el área
print(f"El área del rectángulo es: {rectangulo.calcular_area():.2f}")




