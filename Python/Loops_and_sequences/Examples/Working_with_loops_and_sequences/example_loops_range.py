print('What Are Ranges and How Can You Use Them in a Loop?\n') # range() no acepta número flotantes o float()

print('Ejemplo 1 de range():')
for num in range(3): # Imprime números desde 0 hasta el 2
    print(num)

print('\nEjemplo 2 de range():')
for num in range(1, 5): # Imprime números desde 1 hasta el 4
    print(num)

print('\nEjemplo 3 de range():')
for num in range(2, 11, 2): # Imprime números desde el 2 hasta el 10 con paso 2
    print(num)

print('\nEjemplo 4 de range():')
for num in range(40, 0, -10): # Imprime una secuencia de números en orden decreciente
    print(num)

print('\nEjemplo 5 de range():')
numbers = list(range(2, 11, 2)) # Podemos crear una lista de números usando range()
print(f'Lista de números creada con range(): {numbers}') # 2, 4, 6, 8, 10]
