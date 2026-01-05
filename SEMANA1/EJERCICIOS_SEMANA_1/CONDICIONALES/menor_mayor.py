"""Pide una edad:

si es menor a 18 → “Menor de edad”

si no → “Mayor de edad”"""

while True:
    try:
        edad = float(input("Ingrese su edad: "))

        if edad < 18:
            print("Menor de edad")
        else:
            print("Mayor de edad")
        break
        
    except ValueError:
        print("Ingresa un numero valido")
    