'''Ejercicio 4 — Practica contextual médica

Evalúa:
¿Qué imprime este código?'''

ferritina = 18
sexo = "f"

if sexo == "f" and ferritina < 30:
    print("Sospecha de déficit de hierro")
else:
    print("Niveles aceptables")

# Solución correcta: Imprime "Sospecha de déficit de hierro" porque ambas condiciones son verdaderas.

'''Ejercicio 4 — Avanzado

# Enunciado:
# Clasifica el riesgo clínico aproximado usando PA, frecuencia cardiaca y saturación de O2:
# - Si SpO2 < 90 -> "Emergencia: hipoxemia severa"
# - Si PAS < 90 o FC > 130 -> "Emergencia: shock/taquicardia extrema"
# - Si PAS >= 180 o PAD >= 120 -> "Urgencia hipertensiva"
# - Si 90 <= SpO2 < 94 -> "Vigilancia: hipoxemia leve"
# - En cualquier otro caso -> "Estable"'''

pas = 92   # presión arterial sistólica (mmHg)
pad = 58   # presión arterial diastólica (mmHg)
fc = 118   # frecuencia cardiaca (lpm)
spo2 = 93  # saturación de oxígeno (%)

if spo2 < 90:
    print("Emergencia: hipoxemia severa")
elif pas < 90 or fc > 130:
    print("Emergencia: shock/taquicardia extrema")
elif pas >= 180 or pad >= 120:
    print("Urgencia hipertensiva")
elif 90 <= spo2 < 94:
    print("Vigilancia: hipoxemia leve")
else:
    print("Estable")

# Pregunta:
# ¿Qué imprime este código con los valores actuales?

# Solución correcta: Imprime "Vigilancia: hipoxemia leve" porque la condición 90 <= SpO2 < 94 es verdadera con SpO2 = 93.