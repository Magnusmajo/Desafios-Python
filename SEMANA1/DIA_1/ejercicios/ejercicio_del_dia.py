'''Mini proyecto del Día 1: CALCULADORA SIMPLE

Este proyecto fija la base para todo lo que viene.

📌 Instrucciones:

Crea un programa que:

Pida dos números

Pida la operación: suma, resta, multiplicación, división

Devuelva el resultado

NO se rompa si el usuario pone algo inesperado'''

num1 = input("Ingresa el primer numero: ")

# Detectar si tiene signo
if num1.startswith(('-', '+')):
    num1_sin_signo = num1[1:]
else:
    num1_sin_signo = num1

# Validar que no quede vacío ni solo un punto
if num1_sin_signo == '' or num1_sin_signo == '.':
    print("Error: El primer numero no es valido.")
    exit()

# Validar puntos decimales
if num1_sin_signo.count('.') > 1:
    print("Error: El primer numero no es valido.")
    exit()

# Validar cada carácter
for i in num1_sin_signo:
    if not (i.isdigit() or i == '.'):
        print("Error: El primer numero no es valido.")
        exit()

# Convertir a número
num1 = float(num1)

print(f"Primer numero valido: {num1}")

num2 = input("Ingresa el segundo numero: ")

# Detectar si tiene signo
if num2.startswith(('-', '+')):
    num2_sin_signo = num2[1:]
else:
    num2_sin_signo = num2

# Validar que no quede vacío ni solo un punto
if num2_sin_signo == '' or num2_sin_signo == '.':
    print("Error: El segundo numero no es valido.")
    exit()

# Validar puntos decimales
if num2_sin_signo.count('.') > 1:
    print("Error: El segundo numero no es valido.")
    exit()

# Validar cada carácter
for i in num2_sin_signo:
    if not (i.isdigit() or i == '.'):
        print("Error: El segundo numero no es valido.")
        exit()

num2 = float(num2)

# <-------Hasta acá es la validación de números (Pero se repite código. No es Buena Práctica)--------->
# Mas adelante veremos cómo evitar repetir código. ------------->

# Validemos la operación
operacion = input("Ingresa la operacion (suma, resta, multiplicacion, division): ").strip().lower()

if operacion not in ['suma', 'resta', 'multiplicacion', 'division', '+', '-', '*', '/']:
    print("Error: La operacion no es valida.")
    exit()

# Realizar la operación
if operacion in ['suma', '+']:
    resultado = num1 + num2
elif operacion in ['resta', '-']:
    resultado = num1 - num2
elif operacion in ['multiplicacion', '*']:
    resultado = num1 * num2
elif operacion in ['division', '/']:
    if num2 == 0:
        print("Error: No se puede dividir por cero.")
        exit()
    resultado = num1 / num2

print(f"El resultado de la {operacion} es: {resultado}")
