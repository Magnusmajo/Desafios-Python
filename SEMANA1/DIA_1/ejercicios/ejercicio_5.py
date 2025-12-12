'''Ejercicio 5 — Mini práctica médica

¿Qué imprime este código?

edad = 55
fumador = True

riesgo = (edad > 50) and fumador

print("Riesgo alto:", riesgo)


Imprime: True
'''

#Para comprobar los resultados, puedes ejecutar este código en un entorno de Python. (F5 en VSCode)

edad = 55
fumador = True
riesgo = (edad > 50) and fumador
print("Riesgo alto:", riesgo)

#Hagámoslo un poco mas interactivo:

edad = input("Introduce la edad del paciente: ")
fumador = input("¿Es fumador? (si/no): ")
riesgo  = (int(edad) > 50) and (fumador.lower() == "si")

if riesgo == True:
    print("Riesgo alto: Sí")
else:
    print("Riesgo alto: No")