'''Mini proyecto del Día 1: CALCULADORA SIMPLE

Este proyecto fija la base para todo lo que viene.

📌 Instrucciones:

Crea un programa que:

Pida dos números

Pida la operación: suma, resta, multiplicación, división

Devuelva el resultado

NO se rompa si el usuario pone algo inesperado'''

def validar_numero(texto):
    """Valida que el texto sea un número válido (entero o decimal)"""
    if not texto or texto == ".":
        return False
    
    # Contar puntos decimales
    puntos = texto.count(".")
    if puntos > 1:
        return False
    
    # Verificar que todos los caracteres sean dígitos o un punto
    for i in texto:
        if not (i.isdigit() or i == "."):
            return False
    
    return True

def obtener_numero(mensaje):
    """Solicita un número al usuario y valida que sea correcto"""
    while True:
        entrada = input(mensaje)
        if validar_numero(entrada):
            return float(entrada)
        else:
            print("Error: Ingresa un número válido")

# Solicitar los números
num1 = obtener_numero("Ingresa el primer numero: ")
num2 = obtener_numero("Ingresa el segundo numero: ")

# Solicitar la operación
operacion = input("Ingresa la operacion que quieres realizar (suma, resta, multiplicacion, division): ").lower().strip()

# Realizar la operación solicitada
if operacion == "suma":
    resultado = num1 + num2
    print(f"La suma de {num1} + {num2} = {resultado}")
elif operacion == "resta":
    resultado = num1 - num2
    print(f"La resta de {num1} - {num2} = {resultado}")
elif operacion == "multiplicacion":
    resultado = num1 * num2
    print(f"La multiplicacion de {num1} * {num2} = {resultado}")
elif operacion == "division":
    if num2 != 0:
        resultado = num1 / num2
        print(f"La division de {num1} / {num2} = {resultado}")
    else:
        print("Error: No se puede dividir entre cero")
else:
    print(f"Error: Operacion '{operacion}' no reconocida. Usa: suma, resta, multiplicacion, division")