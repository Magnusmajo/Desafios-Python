# 5 Recorre una lista de números e ignora los negativos usando `continue`.

numeros = [10, -5, 3, -1, 7, -2, 0, 4]

for i in numeros:
    if i < 0:
        continue
    print(i)