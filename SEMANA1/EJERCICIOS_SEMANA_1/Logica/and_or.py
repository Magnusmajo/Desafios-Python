"""Pide edad y peso.
Muestra “Apto” si edad ≥ 18 y peso ≥ 50."""


while True:
    try:
        edad = float(input("Ingresa tu edad: "))
        peso = float(input("Ingresa tu peso: "))

        if edad >= 18 and peso >= 50:
            print("Apto")
        else:
            print("No apto")
        
        break
    
    except ValueError:
        print("Ingresa un numero válido")