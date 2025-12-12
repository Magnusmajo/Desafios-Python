'''Ejercicio 5 — Escribe tú la solución


Crear una función que reciba la edad y devuelva:

“niño” si < 13

“adolescente” si 13–17

“adulto” si ≥ 18
'''


def clasificar_edad(edad):
    if edad < 13:
        print("niño")
    elif 13 <= edad <= 17:
        print("adolescente")
    else:
        print("adulto")

# Pruebas
clasificador = input("Ingresa la edad: ")

# Validar que la entrada sea un número entero no negativo
if not clasificador.isdigit():
    print("Error: La edad debe ser un número entero no negativo.")
else:
    edad = int(clasificador)
    clasificar_edad(edad)


''' .isdigit() → True o False
Devuelve True cuando:

La cadena contiene solo dígitos del 0 al 9
(no acepta espacios, signos, puntos, letras, ni nada más).

Ejemplos:

"5".isdigit()        # True
"12345".isdigit()    # True
"00089".isdigit()    # True

❌ Devuelve False cuando:

La cadena incluye cualquier otro caracter que no sea un dígito.

Ejemplos:

"-5".isdigit()       # False (el signo no es dígito)
"3.14".isdigit()     # False (el punto no es dígito)
"5a".isdigit()       # False (letra)
" 10".isdigit()      # False (espacio)
"".isdigit()         # False (cadena vacía)'''