"""Función que reciba una nota y devuelva “Aprobado” o “Reprobado”."""

def recibir_nota(nota):
    if not 0 <= nota <= 100:
        raise ValueError("Nota fuera de rango")
    return "Aprobado" if nota >= 60 else "Reprobado"

while True:
    try:
        nota = float(input("Ingrese la nota del estudiante: "))
        print(recibir_nota(nota))
        break
    except ValueError as e:
        print(e)


# <--- Validación fuera de la funció --->
# def recibir_nota(nota):
#     if not 0 <= nota <= 100:
#         return None
#     return "Aprobado" if nota >= 60 else "Reprobado"

# while True:
#     try:
#         nota = float(input("Ingrese la nota del estudiante: "))
#         resultado = recibir_nota(nota)
        
#         if resultado is None:
#             print("Nota fuera de rango (0 - 100)")
#             continue
        
#         print(resultado)
#         break
#     except ValueError:
#         print("Ingresa un número válido")
