#  Que imprime?

for i in range(10):
    if i > 4:
        break
    print(i)
    

# Imprime los números del 0 al 4.
# Explicación: La función range(10) genera una secuencia de números desde 0 hasta 9 (10 no incluido).
# El bucle for itera sobre estos números y en cada iteración verifica si el valor de i es mayor que 4.
# Cuando i es mayor que 4, la instrucción break se ejecuta, lo que hace que el bucle termine inmediatamente, deteniendo cualquier impresión adicional.
