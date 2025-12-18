#  Que imprime?

for i in range(5):
    if i == 3:
        continue
    print(i)

# Imprime los números del 0 al 4, excepto el 3.
# Explicación: La función range(5) genera una secuencia de números desde 0 hasta 4 (5 no incluido).
# El bucle for itera sobre estos números y en cada iteración verifica si el valor de i es igual a 3.
# Si i es 3, la instrucción continue se ejecuta, lo que hace que el bucle salte la impresión de ese número y continúe con la siguiente iteración.