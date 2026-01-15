"""Recorre una palabra y corta cuando aparezca la letra "x"."""

palabra = "Hola experimento 626"

for i in palabra:
    if i == "x":
        break
    print(i, end="")
