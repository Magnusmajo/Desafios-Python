""" 1. Presentación personal (prints)
Crea 01_presentación.py que imprima 3 líneas: nombre, edad y para qué querés aprender a programar."""

nombre = input("Cómo te llamas?: ")
edad = input("Cuantos años tienes?: ")
motivo = input("Para qué quieres aprender a programar?: ")
print(f"Hola!, mi nombre es {nombre}, tengo {edad} años de edad y quiero aprender a programar porque {motivo.lower()}")