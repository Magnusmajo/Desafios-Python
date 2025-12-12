'''Mini proyecto del Día 2: Sistema de Diagnóstico Simple

Este proyecto te ayuda a pensar como backend, pero simple.
'''

# Código base que debes completar:

print("=== SISTEMA DE DIAGNÓSTICO SIMPLE ===")

edad = int(input("Edad del paciente: "))
fiebre = input("¿Tiene fiebre? (s/n): ").lower()
tos = input("¿Tiene tos? (s/n): ").lower()
dolor = input("¿Tiene dolor corporal? (s/n): ").lower()

# Convierte a booleanos
fiebre = fiebre == "s"
tos = tos == "s"
dolor = dolor == "s"

# Lógica principal
if fiebre and tos and dolor:
    diagnostico = "Posible cuadro viral"
elif fiebre and tos:
    diagnostico = "Posible infección respiratoria"
elif fiebre and not tos:
    diagnostico = "Hipertermia o fiebre aislada"
else:
    diagnostico = "Sin signos de alarma"

# Casos extra
if edad > 65 and fiebre:
    diagnostico += " (riesgo por edad)"

print("Diagnóstico sugerido:", diagnostico)