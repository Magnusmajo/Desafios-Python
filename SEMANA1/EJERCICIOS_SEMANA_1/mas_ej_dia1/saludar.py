"""Pide un nombre y muestra:
Hola, <nombre>"""

#<--------------- Saludar ------------>

while True:
    user = input("Hola, Como te llamas? ")
    if not user.isalpha():
        print("Por favor, ingresa tu nombre real, solo letras")
    else:
        print(f"Hola {user}")
        break