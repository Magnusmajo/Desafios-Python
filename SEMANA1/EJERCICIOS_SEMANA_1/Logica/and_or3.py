"""Pide una contraseña.
Muestra “Inválida” si no es igual a "admin"."""

while True:
    password = input("Ingresa tu contraseña: ")
    
    if password == "admin":
        print("Acceso concedido")
        break
    else:
        print("Inválida, Intenta de nuevo")
