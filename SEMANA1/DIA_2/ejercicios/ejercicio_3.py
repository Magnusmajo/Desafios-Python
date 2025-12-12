'''Ejercicio 3 — Lógicos

Evalúa:
¿Qué imprime este código?
'''


temperatura = 37.8
tiene_sintomas = True

if temperatura > 37.5 or tiene_sintomas:
    print("Posible fiebre o infección")
else:
    print("Normal")

# Solución correcta: Imprime "Posible fiebre o infección" porque la condición es verdadera (ambas subcondiciones son verdaderas).

'''Ejercicio 3 — Avanzado
Valide que el usuario ingrese dos números válidos (enteros o decimales).
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

num2 = input("Ingresa el primer numero: ")

# Detectar si tiene signo
if num2.startswith(('-', '+')):
    num2_sin_signo = num2[1:]
else:
    num2_sin_signo = num2

# Validar que no quede vacío ni solo un punto
if num2_sin_signo == '' or num2_sin_signo == '.':
    print("Error: El primer numero no es valido.")
    exit()

# Validar puntos decimales
if num2_sin_signo.count('.') > 1:
    print("Error: El primer numero no es valido.")
    exit()

# Validar cada carácter
for i in num2_sin_signo:
    if not (i.isdigit() or i == '.'):
        print("Error: El primer numero no es valido.")
        exit()

# Imprimir número válido
print(f"Primer numero valido: {num1}")
print(f"Segundo numero valido: {num2}")

