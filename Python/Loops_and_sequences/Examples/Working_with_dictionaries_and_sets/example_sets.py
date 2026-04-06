print('What Are Sets, and How Do They Work?\n')

print('Ejemplo 1 de set:')
my_set = {1, 2, 3, 4, 5}
print(f'My first set: {my_set}')

my_set.add(6)
print(f'6 add in my set: {my_set}')

print('\nNo admite duplicados')
print('Para eliminar elementos podemos usar remove() o discard()')
print('remove() devuelve KeyError si no encuentra el valor')
print('discard() no devuelve nada si no se encuentra el valor')

print('\nEjemplo de eliminar un elemento en un set:')
my_set.remove(4)
print(f'My set: {my_set}')

my_set.discard(4)
print(f'My set: {my_set}')

print('\nclear() elimina todos los elementos del set')

print('\nEjemplo con issubset() y issuperset()')
print('Estos métodos comprueban si un conjunto (set) es un subconjunto o un superconjunto de otro conjunto')
my_set = {1, 2, 3, 4, 5}
your_set = {2, 3, 4, 5, 6}

print(f'{my_set} es un subconjunto de {your_set}: {my_set.issubset(your_set)}')
print(f'{my_set} es un superconjunto de {your_set}: {my_set.issuperset(your_set)}')
print(f'{your_set} es un subconjunto de {my_set}: {your_set.issubset(my_set)}')
print(f'{your_set} es un superconjunto de {my_set} {your_set.issuperset(my_set)}')

print('\nEjemplo con isdisjoint():')
print('Este método comprueba si dos conjuntos están separados, lo que significa que no tienen ningún elemento en común')
print(f'{my_set} no tiene algo en común con {your_set}: {my_set.isdisjoint(your_set)}')

print('\nEjemplo con |')
print('Este operador devuelve un nuevo conjunto con todos los elementos de ambos conjuntos')
print(f'My set: {my_set}')
print(f'Your set: {your_set}')
print(f'Set con ambos valores de my_set y your_set: {my_set | your_set}')

print('\nEjemplo con &')
print('Este operador devuelve un nuevo conjunto con solo los elementos comunes de ambos sets')
print(f'My set: {my_set}')
print(f'Your set: {your_set}')
print(f'Set con valores comunes de my_set y your_set: {my_set & your_set}')

print('\nEjemplo con -')
print('Este operador devuelve un nuevo conjunto con los elementos del primer conjunto que no están en los otros conjuntos')
print(f'My set: {my_set}')
print(f'Your set: {your_set}')
print(f'Set con valores de my_set que no están en your_set: {my_set - your_set}')

print('\nEjemplo con ^')
print('Este operador devuelve un nuevo conjunto con los elementos que están en my_set y en your_set pero no en ambos')
print(f'My set: {my_set}')
print(f'Your set: {your_set}')
print(f'Set con valores que están en my_set y en your_set pero no en ambos: {my_set ^ your_set}')

print('\nEjemplo de comprobación si un set contiene un valor:')
print(f'My set: {my_set}')
print(f'My set contiene 5: {5 in my_set}')
