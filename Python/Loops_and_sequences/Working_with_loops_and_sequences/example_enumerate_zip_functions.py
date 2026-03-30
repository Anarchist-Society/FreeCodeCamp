print('What Are the Enumerate and Zip Functions and How Do They Work?\n')

print('Ejemplo 1:')
languages = ['Spanish', 'English', 'Russian', 'Chinese']
print(f'Lista inicial: {languages}')

print('\nRecorremos valores de la lista con un bucle for:')
for language in languages:
    print(language)

# Problema, queremos realizar un seguimiento de índice:
languages = ['Spanish', 'English', 'Russian', 'Chinese']
print(f'\nLista inicial: {languages}')

print('\nRecorremos los valores de la lista con un bucle for y mostramos el índice:')
index = 0
for language in languages:
    print(f'Index {index} and language {language}')
    index += 1

print('\nEjemplo 1: enumerate():')
languages = ['Spanish', 'English', 'Russian', 'Chinese']
print(f'Lista inicial: {languages}')
print(list(enumerate(languages)))

print('\nEjemplo 2: enumerate():')
languages = ['Spanish', 'English', 'Russian', 'Chinese']
print(f'Lista inicial: {languages}')

print('\nRecorremos los valores de la lista con un bucle for y mostramos el índice gracias a enumerate:')
for index, language in enumerate(languages):
    print(f'Index {index} and language {language}')

print('\nEjemplo 3: enumerate():')
languages = ['Spanish', 'English', 'Russian', 'Chinese']
print(f'Lista inicial: {languages}')

print('\nRecorremos los valores de la lista con un bucle for y mostramos el índice gracias a enumerate:')
for index, language in enumerate(languages, 1):
    print(f'Index {index} and language {language}') # Le estamos diciendo que empieze el índice desde el 1

print('\nEjemplo 1: zip():')
developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
print(f'Lista developers: {developers}')
ids = [1, 2, 3, 4]
print(f'Lista de ids: {ids}')

print(f'Listas combinadas con zip(): {list(zip(developers, ids))}') # zip sirve para combinar 2 listas y convertirlas en 1 tuplas

print('\nEjemplo 2: zip():')
developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
print(f'Lista developers: {developers}')
ids = [1, 2, 3, 4]
print(f'Lista de ids: {ids}')

print('\nEjemplo de mostrar valores con zip:')
for name, id in zip (developers, ids):
    print(f'Name: {name}')
    print(f'ID: {id}')
