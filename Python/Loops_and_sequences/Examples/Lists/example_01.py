print('Ejemplo 1:')

cities = ['Los Angeles', 'London', 'Tokyo']
print('El primer valor:', cities[0]) # 'Los Angeles'
print('El último valor:', cities[-1]) # 'Tokyo'

print('\nEjemplo 2:')

developer = 'Jessica'
print('Casting a list:', list(developer)) # ['J', 'e', 's', 's', 'i', 'c', 'a']

numbers = [1, 2, 3, 4, 5]
print('Longitud de la lista:', len(numbers)) # 5

programming_languages = ['Python', 'Java', 'C++', 'Rust']
print('Lista antes:', programming_languages)
programming_languages[0] = 'JavaScript'
print('Las listas son mutables:', programming_languages) # ['JavaScript', 'Java', 'C++', 'Rust']

developers = ['Jane Doe', 23, 'Python Developer']
print('Lista antes:', developers)

del developers[1]
print('Lista después de eliminar un elemento:', developers) # ['Jane Doe', 'Python Developer']

programming_languages = ['Python', 'Java', 'C++', 'Rust']
print('Rust en la lista?:', 'Rust' in programming_languages) # True
print('JavaScript en la lista?:', 'JavaScript' in programming_languages) # False

developer = ['Alice', 25, ['Python', 'Rust', 'C++']]
print('Valores de la lista anidada:', developer[2]) # ['Python', 'Rust', 'C++']
print('Valor de la lista anidada:', developer[2][1]) # 'Rust'

developer = ['Alice', 34, 'Rust Developer']
name, age, job = developer
print(name) # 'Alice'
print(age) # 34
print(job) # 'Rust Developer'

developer = ['Alice', 34, 'Rust Developer']
name, *rest = developer
print(name) # 'Alice'
print(*rest) # [34, 'Rust Developer']

desserts = ['Cake', 'Cookies', 'Ice Cream', 'Pie', 'Brownies']
print(desserts[1:4]) # ['Cookies', 'Ice Cream', 'Pie']

numbers = [1, 2, 3, 4, 5, 6]
print(numbers[1::2]) # [2, 4, 6]
