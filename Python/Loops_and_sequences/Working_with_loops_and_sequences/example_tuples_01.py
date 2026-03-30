print('What Are Tuples and How Do They Work?\n')

print('Ejemplo 1:') # Las tuplas es un tipo de dato para crear un sequencia de valores ordenados
developer = ('Alice', 34, 'Rust Developer')
print(f'Tupla inicial: {developer}')

# Las tuplas son un tipo de dato inmutable a diferencia de las lista que son mutables, es decir que se pueden cambiar los valores

print(f'Accedemos al primer índice de la tupla: {developer[1]}') # 34

# También se puede usar la indexación negativa

print('\nEjemplo 2:')
numbers = (1, 2, 3, 4, 5)
print(f'Tupla inicial: {numbers}')
print(f'Accedemos al -2 índice de la tupla: {numbers[-2]}') # 4

print('\nEjemplo 3:')
developer = 'Jessica'
print(f'Variable inicial: {developer}')
print(f'Podemos convertir un string en una tupla: {tuple(developer)}') # ('J', 'e', 's', 's', 'i', 'c', 'a')

print('\nEjemplo 4:')
programming_languages = ('Python', 'Java', 'C++', 'Rust')
print(f'Tupla inicial: {programming_languages}')
print(f'Podemos comprobar con "in" si rust está en la tupla: {'Rust' in programming_languages}') # True
print(f'Podemos comprobar con "in" si JavaScript está en la tupla: {'JavaScript' in programming_languages}') # False

print('\nEjemplo 5:') # Podemos descomprimir la tupla al igual que con las listas
developer = ('Alice', 34, 'Rust Developer')
print(f'Tupla inicial: {developer}')
name, age, job = developer
print(f'Name: {name}') # 'Alice'
print(f'Age: {age}') # 34
print(f'Job: {job}') # 'Rust Developer'

print('\nEjemplo 6:') # También podemos recopilar los elementos restantes
developer = ('Alice', 34, 'Rust Developer')
name, *rest = developer

print(f'Tupla inicial: {developer}')
print(f'Name: {name}') # 'Alice'
print('Resto:', *rest) # [34, 'Rust Developer']

print('\nEjemplo 7:') # Al igual que con las listas, podemos usar un operador de corte para extraer una parte de ella
desserts = ('cake', 'pie', 'cookies', 'ice cream')
print(f'Tupla inicial: {desserts}')
print(f'Lista filtrada entre 1 y 3 índice: {desserts[1:3]}') # ('pie', 'cookies')
