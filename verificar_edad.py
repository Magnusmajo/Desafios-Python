"""Pide una edad e indica si es igual a 18."""

while True:
    try:
        edad = float(input("Ingresa tu edad: "))
        if edad > 18:
            print("Estas mayorcito chiquilin")
        elif edad < 18:
            print("Lo sentimos, no cambiamos pañales")
        else:
            print("Genial, ya sos grande!")
        break
    except ValueError:
        print("Ingrese un número válido")