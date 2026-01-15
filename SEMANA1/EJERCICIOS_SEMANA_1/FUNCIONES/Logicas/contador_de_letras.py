"""Función que reciba un texto y cuente cuántas letras tiene."""


def contador(texto):
    suma = 0
    for i in texto:
        if i.isalpha():
            suma += 1
    return suma

texto = contador("Hola, Bienvenido a Python")
print(texto)


#  < ---Si se quiere contar todos los caracteres, incluyendo espacios --->

# def contador(texto):
#     return len(texto)

# print(contador("Hola muñeco"))
