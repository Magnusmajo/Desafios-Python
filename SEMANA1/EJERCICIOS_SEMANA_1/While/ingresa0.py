"""Pide números al usuario hasta que ingrese 0."""

while True:
    try:
        num = float(input("Ingresa un número: "))
        if num == 0:
            print("El número ingresado es 0")
            break
        else:
            print("Nop")
    except ValueError:
        print("Ingresa un número válido")
