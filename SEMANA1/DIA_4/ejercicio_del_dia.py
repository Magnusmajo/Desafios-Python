"""Mini proyecto del Día 4

Archivo: evaluacion_salud.py

Objetivo:

Separar lógica en funciones (como haría un backend real).

Requisitos:

Crear funciones para:

Pedir datos del paciente

Calcular IMC

Clasificar IMC

Mostrar resultado final
"""

def pedir_datos():
    nombre = input("Nombre del paciente: ")
    peso = float(input("Peso en kg: "))
    altura = float(input("Altura en metros: "))
    return nombre, peso, altura


def calcular_imc(peso, altura):
    return peso / (altura ** 2)


def clasificar_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc <= 24.9:
        return "Normal"
    elif 25.0 <= imc <= 29.9:
        return "Sobrepeso"
    elif 30.0 <= imc <= 34.9:
        return "Obesidad"
    else:
        return "Obesidad Grave"


def mostrar_resultado(nombre, imc, clasificacion):
    print("\nResultado de evaluación")
    print(f"Paciente: {nombre}")
    print(f"IMC: {imc:.2f}")
    print(f"Clasificación: {clasificacion}")


# Programa principal
nombre, peso, altura = pedir_datos()
imc = calcular_imc(peso, altura)
clasificacion = clasificar_imc(imc)
mostrar_resultado(nombre, imc, clasificacion)
