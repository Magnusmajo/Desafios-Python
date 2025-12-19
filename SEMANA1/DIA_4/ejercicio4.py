"""Ejercicio 4 — Return vs print

Crea una función que:

reciba dos números

imprima la suma

y otra función que reciba dos números y retorne la suma"""

def imprimir_suma(num1, num2):
    print(num1 + num2)

def retornar_suma(num1, num2):
    return num1 + num2

# Ejemplo de uso
imprimir_suma(5, 10)  # Esto imprimirá 15
resultado = retornar_suma(5, 10)
print(f"La suma retornada es: {resultado}")  # Esto imprimirá "La suma retornada es: 15"