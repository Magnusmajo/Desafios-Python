"""Pide dos números e indica si son distintos."""

while True:
    try:
        num1 = float(input("Ingresa el primer numero: "))
        num2 = float(input("Ingresa el segundo numero: "))

        if num1 != num2:
            print("Son diferentes")
        else:
            print("Son iguales")
        break

    except ValueError:
        print("Ingresa un numero valido")