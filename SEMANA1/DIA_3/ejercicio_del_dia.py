# Simular el llamado de turnos en una clínica.

print("=== SISTEMA DE TURNOS ===")

turnos = int(input("Cantidad de pacientes en espera: "))

while turnos > 0:
    if turnos > 1:
        print(f"Siguiente paciente, quedan {turnos - 1} pacientes en espera.")
    else:
        print("Siguiente paciente, no quedan más pacientes en espera.")
    turnos -= 1
    turnos = int(input("Cantidad de pacientes en espera: "))