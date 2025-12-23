"""Pide un número e indica si es positivo o negativo."""

while True:
    try:
        num = float(input("Ingresa un número: "))
        
        if  num >= 0:
            print(f"{num} es un número positivo")
        else:
            print(f"{num} es un número negativo")
        break
    except ValueError:
        print("Ingresa un número válido")