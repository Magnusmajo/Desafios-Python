# 4 Pide una contraseña con `while` hasta que sea correcta.

while True:
    contraseña = input("Ingresa la contraseña: ")
    if contraseña == "Pepito123":
        print("Acceso concedido")
        break
    else:
        print("Contraseña incorrecta, intenta de nuevo.")