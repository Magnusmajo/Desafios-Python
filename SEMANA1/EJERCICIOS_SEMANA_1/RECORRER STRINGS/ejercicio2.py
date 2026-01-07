"""Cuenta cuántas veces aparece la letra "a" en un texto."""
num = 0
texto = input("Escribe algo: ")

for i in texto:
    if i.lower() == "a":
        num = num + 1

print(num)


# Forma ideal
# texto = input("Escribe algo: ")
# print(texto.lower().count("a"))
