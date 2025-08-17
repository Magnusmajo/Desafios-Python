"""Imprime un pequeño banner de 5–7 líneas (ASCII) con tu nombre dentro.
# Practica \n y varias llamadas a print()."""

#<----Con ancho adaptativo---->
nombre = "Juan Carlos"

# definimos el ancho del banner (será el largo del nombre + 6 espacios extra)
ancho = len(nombre) + 6  

print("*" * ancho)                       # línea superior
print("|" + " " * (ancho - 2) + "|")     # línea en blanco
print("|" + nombre.center(ancho - 2) + "|")  # línea con el nombre centrado
print("|" + " " * (ancho - 2) + "|")     # línea en blanco
print("*" * ancho)                       # línea inferior



#<--------Swgunda forma--------->
# nombre = "Alexis"

# print(
#     "********************\n"
#     "*                  *\n"
#     "*                  *\n"
#     "*" + nombre.center(18) + "*\n"
#     "*                  *\n"
#     "*                  *\n"
#     "********************"
# )
