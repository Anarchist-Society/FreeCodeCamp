print('Ejemplo: count():') # Determina cuántas veces aparece un elemento en una tupla
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
print(f'Tupla inicial: {programming_languages}')
print(f'Número de veces que aparece "Rust:" {programming_languages.count('Rust')}') # 2
print(f'Número de veces que aparece "JavaScript": {programming_languages.count('JavaScript')}') # 0

print('\nEjemplo: index():')
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
programming_languages.index('Java') # 1
