"""Pide una nota (0–10) y muestra:

“Aprobado” si ≥ 6

“Desaprobado” si < 6"""

while True:
    try:
        nota = float(input("Ingresa la nota (0 - 10): "))
        
        if nota >= 6:
            print("Aprobado")
        else:
            print("Suspenso")
        break
    
    except ValueError:
        print("Ingresa un numeo valido entre 0 y 100")