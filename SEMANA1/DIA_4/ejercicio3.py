"""Ejercicio 3 — Condiciones dentro de funciones

Crea una función clasificar_imc(imc) que devuelva:

“Bajo peso”

“Normal”

“Sobrepeso”

“Obesidad”

(según valores estándar)
Bajo peso (<18.5), Normal (18.5-24.9), Sobrepeso (25.0-29.9), Obesidad (>30.0), y Obesidad Grave (>40.0), según la Organización Mundial de la Salud (OMS)
"""

def clasificar_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc <= 24.9:
        return "Normal"
    elif 25.0 <= imc <= 29.9:
        return "Sobrepeso"
    elif imc> 30.0:
        return "Obesidad"
    else:
        return "Obesidad Grave"

# Ejemplo de uso
paciente_alberto = clasificar_imc(30.5)
print(f"El estado de Alberto es: {paciente_alberto}") # Debería imprimir "El estado de Alberto es: Obesidad"