"""Pide números y suma todos hasta que el usuario ingrese un número negativo."""

suma = 0

while True:
    try:
        num = float(input("Ingresa un número: "))
        if num >= 0:
            suma += num
            print(suma)
        else:
            print("Número negativo: Chao")
            break
    except ValueError:
        print("Debes ingresar un número válido")
