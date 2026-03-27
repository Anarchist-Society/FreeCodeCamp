print('What Are Some Common Methods for Tuples?\n')

print('Ejemplo: count():') # Determina cuántas veces aparece un elemento en una tupla
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
print(f'Tupla inicial: {programming_languages}')
print(f'Número de veces que aparece "Rust:" {programming_languages.count('Rust')}') # 2
print(f'Número de veces que aparece "JavaScript": {programming_languages.count('JavaScript')}') # 0

print('\nEjemplo: index():') # Le pasas un argumento y lo busca en la tupla y te devuelve su índice
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
print(f'Tupla inicial: {programming_languages}')
print(f'Index Java: {programming_languages.index('Java')}') # 1

programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
print(f'\nTupla inicial: {programming_languages}')
print(f'Index Python: {programming_languages.index('Python', 3)}') # 5 porque al pasar un segundo argumento le decimos a la funcion desde donde empezar a buscar

programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python', 'JavaScript', 'Python')
print(f'\nTupla inicial: {programming_languages}')
print(f'Index Python: {programming_languages.index('Python', 2, 5)}') # 2 porque al pasar el tercer argumento le decimos hasta donde buscar

print('\nEjemplo: sorted():') # Ordenar
numbers = (13, 2, 78, 3, 45, 67, 18, 7)
print(f'Tupla inicial: {numbers}')
print(f'Lista ordenada: {sorted(numbers)}') # La función sorted siempre creará una nueva lista

programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
print(f'\nTupla inicial: {programming_languages}')
print(f'Lista ordenada: {sorted(programming_languages, key=len)}') # En este ejemplo estamos ordenando según la longitud de casa string
# Result
# ['C++', 'Rust', 'Java', 'Rust', 'Python', 'Python']

programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
print(f'\nTupla inicial: {programming_languages}')
print(f'Lista ordenada reverse: {sorted(programming_languages, reverse=True)}') # En este ejemplo estamos ordenando los string por orden alfabético y de forma reversa

# Result
# ['Rust', 'Rust', 'Python', 'Python', 'Java', 'C++']
