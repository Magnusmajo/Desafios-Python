"""
3. Ticket simple
imprime un “recibo” de 4 líneas:
  - Título “Tienda XYZ”
  - Fecha (puede ser una string fija hoy)
  - Ítem y precio
  - “Total:”
En esta etapa solo print(); no uses input aún.
"""

# TITULO = "Tienda XYZ"
# fecha = "2025-08-15"
# item = "Café"
# precio = 2.50

#<----------------------------------------------------->
# # usando f-strings
# print(
#     f"{TITULO:^30}\n"
#     f"Fecha: {fecha}\n"
#     f"{item:<20} ${precio:>7.2f}\n"
#     f"{'Total:':<20} ${precio:>7.2f}"
#)

#<-------------------------------------------------------->
# # usando .format()
# print("Titulo : {} \nFecha : {} \n Item : {} \n Precio : {} \n Total : {}".format(titulo, fecha, item, precio, precio))

#<-------------------------------------------------------->
# # usando concatenación
# print("Titulo : " + titulo + " \nFecha : " + fecha + " \n Item : " + item + " \n Precio : " + str(precio) + " \n Total : " + str(precio))

#<---------------------------------------------------------->
"""Tickets profesional
Construcción de un ticket de compra
Crea un ticket de compra que incluya:
- Título de la tienda
- Fecha de compra
- Ítems comprados (nombre y precio)
- Total a pagar
"""
# # Datos de la tienda y fecha
# TITULO = "Tienda La Única"
# FECHA = "2025-08-15"

# # Lista para guardar los ítems
# items = []

# # Pedimos al usuario cuántos ítems va a agregar
# while True:
#     try:
#         cantidad = int(input("¿Cuántos ítems desea ingresar?: "))
#         if cantidad > 0:
#             break
#         else:
#             print("Debe ingresar al menos 1 ítem.")
#     except ValueError:
#         print("Ingrese un número válido.")

# # Recolectamos cada ítem
# for i in range(cantidad):
#     nombre = input(f"Nombre del ítem {i+1}: ")
#     while True:
#         try:
#             precio = float(input(f"Precio del ítem {i+1}: "))
#             break
#         except ValueError:
#             print("Ingrese un precio válido (número).")
#     items.append({"nombre": nombre, "precio": precio})

# # Construimos el ticket
# total = 0
# ticket = f"{TITULO:^30}\nFecha: {FECHA}\n"
# ticket += "-" * 30 + "\n"

# for item in items:
#     ticket += f"{item['nombre']:<20} ${item['precio']:>7.2f}\n"
#     total += item['precio']

# ticket += "-" * 30 + "\n"
# ticket += f"{'TOTAL':<20} ${total:>7.2f}"

# # Imprimimos todo el ticket
# print(ticket)
