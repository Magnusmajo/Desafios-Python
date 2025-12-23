"""Pide dos números e indica si el primero es mayor que el segundo."""

while True:
    try:
        numero1 = float(input("Ingresa el primer número: "))
        numero2 = float(input("Ingresa el segundo número: "))
        if numero1 > numero2:
            print(f"{numero1} es mayor que {numero2}")
        elif numero1 < numero2:
            print(f"{numero1} es menor que {numero2}")
        else:
            print(f"{numero1} y {numero2} son iguales")
        break
    except ValueError:
        print("Debes ingresar un número válido") 
