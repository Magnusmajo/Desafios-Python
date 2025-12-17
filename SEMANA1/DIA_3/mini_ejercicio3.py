#3 Recorre un string e imprime solo las vocales.

texto = "Desafío Python"
for caracter in texto:
    if caracter.lower() in 'aeiou':
        print(caracter)