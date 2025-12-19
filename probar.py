def agregar_item(item, lista=[]):
    lista.append(item)
    return lista

items = agregar_item('manzana, banana, coco')
print(items)  # Salida esperada: ['manzana, banana, coco']
items = agregar_item('naranja')
print(items)  # Salida esperada: ['naranja']
