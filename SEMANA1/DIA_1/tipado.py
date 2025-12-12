# Tipado dinámico en Python

'''Definición: En un lenguaje de tipado dinámico, como Python, el tipo se asocia al valor en memoria y no a la variable. La variable es solo una referencia reutilizable que puede apuntar a valores de distinto tipo durante la ejecución.
Asignaciones flexibles: Puedes reasignar la misma variable a valores de tipos diferentes sin redeclaraciones. 
Ejemplo:
    '''
numero = 42          # int
numero = 3.14        # float
numero = "cuarenta"  # str

'''Resolución en tiempo de ejecución: Las comprobaciones de tipo ocurren cuando el programa corre, no al compilarse. Esto agiliza la escritura, pero desplaza los errores hacia el runtime.
Gotcha habitual: Operaciones que dependen de un tipo específico pueden fallar si la variable cambió a un tipo distinto:
'''
resultado = "5" + 3   # TypeError en tiempo de ejecución

'''Ventajas:
- Flexibilidad: Permite escribir código más rápido y con menos restricciones.
- Prototipado rápido: Ideal para desarrollo ágil y pruebas rápidas de conceptos.
Desventajas:
- Errores en tiempo de ejecución: Los errores de tipo pueden surgir durante la ejecución, dificultando la depuración.
- Mantenimiento: El código puede volverse difícil de entender si las variables cambian de tipo frecuentemente.
Conclusión: El tipado dinámico de Python ofrece gran flexibilidad y rapidez en el desarrollo, pero requiere cuidado para evitar errores en tiempo de ejecución y mantener la claridad del código.'''

# Ejemplo de tipado dinámico en Python
variable = 10          # variable es un entero
print(type(variable))  # <class 'int'>

variable = "Hola"     # ahora variable es una cadena
print(type(variable))  # <class 'str'>

variable = [1, 2, 3]  # ahora variable es una lista
print(type(variable))  # <class 'list'>

# Ejemplo de error en tiempo de ejecución debido a tipado dinámico
valor = "10"

try:
    resultado = valor + 5  # TypeError: str + int
except TypeError:
    resultado = int(valor) + 5

print(resultado)  # 15

