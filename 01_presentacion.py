""" 1. Presentación personal (prints)
Crea 01_presentación.py que imprima 3 líneas: nombre, edad y para qué querés aprender a programar."""

nombre = input("Cómo te llamas?: ")
try:
    edad = int(input("Cuantos años tienes?: "))
except ValueError:
    print("Por favor ingresa un número válido para la edad. Solo números.")
    edad = int(input("Cuantos años tienes?: "))
motivo = input("Para qué quieres aprender a programar?: ")

print(f"Hola!, mi nombre es {nombre}, tengo {edad} años de edad y quiero aprender a programar porque {motivo}.")