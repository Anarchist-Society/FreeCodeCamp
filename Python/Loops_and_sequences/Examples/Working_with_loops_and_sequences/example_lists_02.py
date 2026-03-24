print('Ejemplo: append():\n')
numbers = [1, 2, 3, 4, 5]
print('Lista inicial:', numbers)

numbers.append(6) # append() sirve para añadir un elemento al final de una lista
print('Lista después:', numbers, '\n')

numbers = [1, 2, 3, 4, 5]
even_numbers = [6, 8, 10]

# numbers.append(even_numbers)
# print(numbers) # [1, 2, 3, 4, 5, [6, 8, 10]]

print('Ejemplo: extend():')
numbers = [1, 2, 3, 4, 5]
print('Lista inicial:', numbers)

even_numbers = [6, 8, 10]
numbers.extend(even_numbers) # Sive para añadir varios elementos
print('Lista después:', numbers, '\n') # [1, 2, 3, 4, 5, 6, 8, 10]

print('Ejemplo: insert():\n')

numbers = [1, 2, 3, 4, 5]
print('Lista inicial:', numbers)

numbers.insert(2, 4) # Sirve para añadir un elemento en una posición específica de una lista y desplaza los demás elementos
print('Lista después:', numbers, '\n') # [1, 2, 4, 3, 4, 5]

print('Ejemplo: remove():\n')

numbers = [10, 20, 30, 40,50, 50]
print('Lista inicial:', numbers)

numbers.remove(50) # Elimina por valor y no devuelve nada
print('Lista después:', numbers, '\n')

print('Ejemplo: pop():\n')

numbers = [1, 2, 3, 4, 5]
print('Lista inicial:', numbers)

numbers.pop(1) # The number 2 is returned Elimina por índice y devuelve valor
print('Lista después:', numbers, '\n')

print('Ejemplo: clear():\n')

numbers = [1, 2, 3, 4, 5]
print('Lista inicial:', numbers)

numbers.clear() # Vaciar completamenta la lista
print('Lista después:', numbers, '\n')# []

print('Ejemplo: sort():\n')
numbers = [19, 2, 35, 1, 67, 41]
print(f'Lista inicial: {numbers}')

numbers.sort() # Ordenar la lista original y no devuelve nada
print(f'Lista después: {numbers} \n') # [1, 2, 19, 35, 41, 67]

print('Ejemplo: sorted():\n')

numbers = [19, 2, 35, 1, 67, 41]
sorted_numbers = sorted(numbers) # Ordenar la lista y devuelve una nueva lista, no ordena la lista original

print('Lista con valores desordenados:', numbers) # [19, 2, 35, 1, 67, 41]
print('Lista con valores ordenados:', sorted_numbers, '\n') # [1, 2, 19, 35, 41, 67]

print('Ejemplo: reverse():\n')

numbers = [6, 5, 4, 3, 2, 1]
print(f'Lista inicial: {numbers}')

numbers.reverse() # Invierte el orden de los elementos en una lista y no devuelve nada
print(f'Lista después: {numbers} \n') # [1, 2, 3, 4, 5, 6]

print('Ejemplo: index():\n')

programming_languages = ['Rust', 'Java', 'Python', 'C++']
print(f'Lista inicial: {programming_languages}')

print(f'Indice donde se encuentra java: {programming_languages.index('Java')}') # 1
