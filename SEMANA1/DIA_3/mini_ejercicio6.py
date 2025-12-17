# 6 Busca un número en una lista y usa `break` cuando lo encuentres.

numeros = [10, 23, 45, 67, 89, 23, 45, 90]

numero_a_buscar = 45
for numero in numeros:
    if numero == numero_a_buscar:
        print(f"Número {numero_a_buscar} encontrado en la lista.")
        break