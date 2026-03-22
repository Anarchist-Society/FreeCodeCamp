print('append():\n')

numbers = [1, 2, 3, 4, 5]
print('Lista inicial:', numbers)

numbers.append(6)
print('Lista después:', numbers, '\n')

numbers = [1, 2, 3, 4, 5]
even_numbers = [6, 8, 10]

# numbers.append(even_numbers)
# print(numbers) # [1, 2, 3, 4, 5, [6, 8, 10]]

numbers = [1, 2, 3, 4, 5]
print('Lista inicial:', numbers)

even_numbers = [6, 8, 10]
numbers.extend(even_numbers)
print('Lista después:', numbers, '\n') # [1, 2, 3, 4, 5, 6, 8, 10]

print('insert():\n')

numbers = [1, 2, 3, 4, 5]
print('Lista inicial:', numbers)

numbers.insert(2, 4)
print('Lista después:', numbers, '\n') # [1, 2, 2.5, 3, 4, 5]

print('remove():\n')

numbers = [10, 20, 30, 40,50, 50]
print('Lista inicial:', numbers)

numbers.remove(50)
print('Lista después:', numbers, '\n')

print('pop():\n')

numbers = [1, 2, 3, 4, 5]
print('Lista inicial:', numbers)

numbers.pop(1) # The number 2 is returned
print('Lista después:', numbers, '\n')

print('clear():\n')

numbers = [1, 2, 3, 4, 5]
print('Lista inicial:', numbers)

numbers.clear()
print('Lista después:', numbers, '\n')# []

print('sort():\n')
numbers = [19, 2, 35, 1, 67, 41]
print(f'Lista inicial: {numbers}')

numbers.sort()
print(f'Lista después: {numbers} \n') # [1, 2, 19, 35, 41, 67]

print('sorted():\n')

numbers = [19, 2, 35, 1, 67, 41]
sorted_numbers = sorted(numbers)

print('Lista con valores desordenados:', numbers) # [19, 2, 35, 1, 67, 41]
print('Lista con valores ordenados:', sorted_numbers, '\n') # [1, 2, 19, 35, 41, 67]

print('reverse():\n')

numbers = [6, 5, 4, 3, 2, 1]
print(f'Lista inicial: {numbers}')

numbers.reverse()
print(f'Lista después: {numbers} \n') # [1, 2, 3, 4, 5, 6]

print('index():\n')

programming_languages = ['Rust', 'Java', 'Python', 'C++']
print(f'Lista inicial: {programming_languages}')

print(f'Indice donde se encuentra java: {programming_languages.index('Java')}') # 1
