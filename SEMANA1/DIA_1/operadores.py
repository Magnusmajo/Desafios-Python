# Operadores esenciales (Aritméticos, Comparación, Lógicos)
a = 10
b = 3

# Aritméticos - realizan suma, resta, multiplicación, división con decimales, división entera, residuo y potencia respectivamente; se usan para cálculos numéricos básicos.
print(f"Aritméticos: suma={a + b}, resta={a - b}, producto={a * b}, "
    f"division={a / b}, division_entera={a // b}, modulo={a % b}, potencia={a ** b}")

# Comparación (devuelven booleanos) - comparan dos valores y devuelven True o False; se emplean para tomar decisiones en condicionales o bucles.
print(f"Comparación: mayor={a > b}, menor={a < b}, igual={a == b}, "
    f"no_igual={a != b}, mayor_igual={a >= b}, menor_igual={a <= b}")

# Lógicos (operan con booleanos) - and, or, not: combinan o invierten booleanos; permiten construir condiciones compuestas como “ambos deben cumplirse”, “al menos uno” o “negar el resultado”.
es_par = (a % 2) == 0
es_divisible_por_tres = (a % 3) == 0
print(f"Lógicos: ambos={es_par and es_divisible_por_tres}, "
    f"al_menos_uno={es_par or es_divisible_por_tres}, negacion={not es_par}")
