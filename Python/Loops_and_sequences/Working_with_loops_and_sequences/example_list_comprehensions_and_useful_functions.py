print('What Are List Comprehensions and What Are Some Useful Functions to Work With Lists?\n')

print('Ejemplo 1:')
even_numbers = []

for num in range(21):
    if num % 2 == 0:
        even_numbers.append(num)

print(f'Ejemplo de una lista con números pares (0, 20) con range(): {even_numbers}')

print('\nEjemplo 2:')
even_numbers = [num for num in range(21) if num % 2 == 0]

print(f'Ejemplo de una lista con números pares (0, 20) con range pero es una sola línea: {even_numbers}')

print('\nEjemplo 3:')
numbers = [1, 2, 3, 4, 5]

result = [(num, 'Even') if num % 2 == 0 else (num, 'Odd') for num in numbers]
print(result)

print('\nEjemplo 4: filter():')
words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']
print(f'Lista inicial: {words}')

def is_long_word(word):
    return len(word) > 4

long_words = list(filter(is_long_word, words))
print(f'Lista filtrada: {long_words}') # ['mountain', 'river', 'cloud']

print('\nEjemplo 5: map():')
celsius = [0, 10, 20, 30, 40]

def to_fahrenheit(temp):
    return (temp * 9/5) + 32

fahrenheit = list(map(to_fahrenheit, celsius))
print(f'{fahrenheit}') # [32.0, 50.0, 68.0, 86.0, 104.0]

print('\nEjemplo 6: sum():')
numbers = [5, 10, 15, 20]
print(f'Lista inicial: {numbers}')
total = sum(numbers)
print(f'Total: {total}') # Result: 50

print('\nEjemplo 7: sum():')
numbers = [5, 10, 15, 20]
print(f'Lista inicial: {numbers}')
total = sum(numbers, 10) # positional argument, la suma empieza desde 10
print(f'Total: {total}')

print('\nEjemplo 8: sum():')
numbers = [5, 10, 15, 20]
print(f'Lista inicial: {numbers}')
total = sum(numbers, start=10) # keyword argument
print(f'Total: {total}')
