"""Pide un número.
Indica si está entre 10 y 20 (inclusive)."""

while True:
    try:
        numero = float(input("Ingresa un numero: "))
        
        if numero >= 10 and numero <= 20:
            print("Está entre 10 y 20")
        else:
            print("No está entre 10 y 20")
        
        break
    
    except ValueError:
        print("Ingresa un número válido")