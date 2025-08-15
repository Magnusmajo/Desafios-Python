""" 1. Presentación personal (prints)
Crea 01_presentación.py que imprima 3 líneas: nombre, edad y para qué querés aprender a programar."""

nombre = input("¿Cómo te llamas?: ")

while True:
    edad_input = input("¿Cuántos años tienes?: ")
    try:
        edad = int(edad_input)
        break
    except ValueError:
        print("❌ Por favor, ingresa solo números enteros.")

motivo = input("¿Para qué quieres aprender a programar?: ")

print(f"Hola, mi nombre es {nombre}, tengo {edad} años y quiero aprender a programar porque {motivo}.")
