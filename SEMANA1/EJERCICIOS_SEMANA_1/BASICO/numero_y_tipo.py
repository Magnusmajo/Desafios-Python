"""Pide un número entero y muestra:

el número

su tipo usando type()"""

while True:
    try:
        numero = float(input("Ingresa un número "))
        print(f"El número es: {numero}")
        print(type(numero))
        break
    except ValueError:
        print("Debes ingresar un número válido")