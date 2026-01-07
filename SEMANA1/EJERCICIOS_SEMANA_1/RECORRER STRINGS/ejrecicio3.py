"""Muestra solo las vocales de una palabra."""

texto = input("Escribe algo: ")

for vocal in texto:
    if vocal.lower() in "aeiou":
        print(vocal)
