print('What Are Lambda Functions and How Do They Work?\n')

print('Ejemplo de función básica:')
def square(num):
    return num ** 2
print(f'4 al cuadrado es: {square(4)}') # 16

print('\nEjemplo de función lambda:')
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f'Números pares de la lista {numbers} usando una función lambda: {even_numbers}')
