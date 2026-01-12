"""Pide una contraseña hasta que sea correcta."""

password = "abcd"

while True:
    text = input("Ingresa tu contraseña: ")
    if text == password:
        print("Acceso concedido")
        break
    else:
        print("Acceso denegado")