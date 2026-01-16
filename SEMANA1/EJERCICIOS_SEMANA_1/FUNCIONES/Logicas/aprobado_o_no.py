"""Función que reciba una nota y devuelva “Aprobado” o “Reprobado”."""

def recibir_nota(nota):
    if not 0 <= nota <= 100:
        return None
    return "Aprobado" if nota >= 60 else "Reprobado"

while True:
    try:
        nota = float(input("Ingrese la nota del estudiante: "))
        resultado = recibir_nota(nota)
        
        if resultado is None:
            print("Nota fuera de rango (0 - 100)")
            continue
        
        print(resultado)
        break
    except ValueError:
        print("Ingresa un número válido")
