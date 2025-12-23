"""Pide un número y muestra:

división entera entre 2

resto de dividirlo entre 2"""

while True:
    try:
        numero = float(input("Ingresa tu número: "))
        division = numero // 2
        resto = numero % 2
        print(f"Para {numero}, su división entera es {division:.0f} y su resto es {resto:.0f}")
        break
    except ValueError:
        print("Debes introducir un número válido")
