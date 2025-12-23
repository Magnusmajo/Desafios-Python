"""Pide dos números e indica si son distintos."""

while True:
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        if num1 == num2:
            print("Son iguales los números que ingresaste")
        else:
            print("Los números que ingresaste son distintos")
        break
    except ValueError:
        print("Debes ingresar números válidos")