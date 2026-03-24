print('Ejemplo 1:')
cities = ['Los Angeles', 'London', 'Tokyo']
print(f'Lista de valores: {cities}')
print('El primer valor:', cities[0]) # 'Los Angeles'
print('El último valor:', cities[-1]) # 'Tokyo'

print('\nEjemplo 2:')
developer = 'Jessica'
print(f'String: {developer}')
print('Casting a list:', list(developer)) # ['J', 'e', 's', 's', 'i', 'c', 'a']

print('\nEjemplo 3:')
numbers = [1, 2, 3, 4, 5]
print(f'Lista de valores: {numbers}')
print('Longitud de la lista:', len(numbers)) # 5

print('\nEjemplo 4:')
programming_languages = ['Python', 'Java', 'C++', 'Rust']
print('Lista antes:', programming_languages)
programming_languages[0] = 'JavaScript'
print('Las listas son mutables:', programming_languages) # ['JavaScript', 'Java', 'C++', 'Rust']

print('\nEjemplo 5:')
developers = ['Jane Doe', 23, 'Python Developer']
print('Lista antes:', developers)
del developers[1] # Elimina por posición o referencia, no devuelve nada, puede borrar variables completas
print('Lista después de eliminar un elemento:', developers) # ['Jane Doe', 'Python Developer']

print('\nEjemplo 6:')
programming_languages = ['Python', 'Java', 'C++', 'Rust']
print(f'Lista de valores:{programming_languages}')
print('Rust en la lista?:', 'Rust' in programming_languages) # True
print('JavaScript en la lista?:', 'JavaScript' in programming_languages) # False

print('\nEjemplo 7:')
developer = ['Alice', 25, ['Python', 'Rust', 'C++']]
print(f'Lista de valores: {developer}')
print('Valores de la lista anidada:', developer[2]) # ['Python', 'Rust', 'C++']
print('Valor de la lista anidada:', developer[2][1]) # 'Rust'

print('\nEjemplo 8:')
developer = ['Alice', 34, 'Rust Developer']
print(f'Developer: {developer}')
name, age, job = developer
print(f'Name: {name}') # 'Alice'
print(f'Age: {age}') # 34
print(f'Job: {job}') # 'Rust Developer'

print('\nEjemplo 9:')
developer = ['Alice', 34, 'Rust Developer']
print(f'Developer: {developer}')
name, *rest = developer
print(f'Name: {name}') # 'Alice'
print('Rest:', rest) # [34, 'Rust Developer']

print('\nEjemplo 10:')
desserts = ['Cake', 'Cookies', 'Ice Cream', 'Pie', 'Brownies']
print(f'Lista de valores: {desserts}')
print(f'Valores filtrados entre 1 y 4: {desserts[1:4]}') # ['Cookies', 'Ice Cream', 'Pie']

print('\nEjemplo 11:')
numbers = [1, 2, 3, 4, 5, 6]
print(f'Lista de números: {numbers}')
print(f'Valores filtrados con paso 2: {numbers[1::2]}') # [2, 4, 6]
