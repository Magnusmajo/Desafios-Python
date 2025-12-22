"""Pide dos números e imprime:

suma

resta

multiplicación

división"""

while True:
    try:
        numero1 = float(input("Ingresa el primer número "))
        numero2 = float(input("Ingresa el segundo número "))
        
        suma = numero1 + numero2
        resta = numero1 - numero2
        multiplicacion = numero1 * numero2
        division = numero1 / numero2
        
        print("\n<------------- Calculando------------>\n")
        print(f"La suma de {numero1} + {numero2} = {suma}")
        print(f"La resta de {numero1} - {numero2} = {suma}")
        print(f"La multiplicaccion  de {numero1} * {numero2} = {suma}")
        print(f"La división de {numero1} / {numero2} = {suma}")
        break
        
    except ValueError:
        print("Debes ingresar números válidos")
    