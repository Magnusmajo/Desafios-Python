"""Ejercicio 5 — Parámetros por defecto

Crea una función saludar_paciente(nombre="Paciente")."""

def saludar_paciente(nombre="Paciente"):
    print(f"Hola, {nombre}. ¡Bienvenido/a al consultorio!")

# Ejemplo de uso
saludar_paciente("Alberto")  # Debería imprimir: Hola, Alberto. ¡Bienvenido/a al consultorio!