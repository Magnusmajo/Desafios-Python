"""Pide dos números decimales y muestra su suma."""

#< ------------- Sumando Flotantes ---------------->

while True:
    try:
        numero1 = float(input("Ingresa el primer numero válido: "))
        numero2 = float(input("Ingresa el segundo numero válido: "))
        
        suma = numero1 + numero2
        print(f"La suma de {numero1} + {numero2} = {suma}")
        break
    except ValueError:
        print("Debes ingresar números válidos")
    

