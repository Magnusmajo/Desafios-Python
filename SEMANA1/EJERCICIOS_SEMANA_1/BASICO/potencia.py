"""Pide un número y muestra su cuadrado usando **."""

while True:
    try:
        numero = float(input("Ingrese un número: "))
        potencia = numero ** 2
        print(f"{numero} elevado al cuadrado = {potencia}")
        break
    except ValueError:
        print(f"Debes ingresar un número válido")