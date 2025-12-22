"""Pide al usuario su edad y muéstrala multiplicada por 2."""

while True:
    user = input("Ingresa tu edad: ")
    if not user.isdigit():
        print("Debes ingresar un numero entero válido")
    else:
        user = int(user)
        edad_doble = user ** 2
        print(f"El doble de tu edad es {edad_doble}")
        break
    