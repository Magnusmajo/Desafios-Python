"""Función que reciba una edad y devuelva si es mayor de edad."""

def es_mayor(edad):
    return "Es mayor de edad" if edad >= 18 else "Aun es menor de edad"

while True:
    try:
        texto = int(input("Ingresa tu edad: "))
        print(es_mayor(texto))
        break
    except ValueError:
        print("Debes ingresar un número válido")