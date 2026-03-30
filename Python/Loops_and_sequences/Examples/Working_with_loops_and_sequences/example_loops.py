print('How Do Loops Work?\n')

programming_languages = ['Rust', 'Java', 'Python', 'C++']
print(f'Lista inicial: {programming_languages}')
print('\nRecorriendo la lista con for:')
for language in programming_languages:
    print(language)

print('\nEjemplo 2 con for:')
for char in 'code':
    print(char)

print('\nEjemplo de bucle anidado:')
categories = ['Fruit', 'Vegetable']
foods = ['Apple', 'Carrot', 'Banana']
print(f'Lista inicial 1: {categories}')
print(f'Lista inicial 2: {foods}')

print('\nEjemplo de bucle anidado:')
for category in categories:
    for food in foods:
        print(category, food)

print('\nEjemplo de bucle while:')
secret_number = 3
guess = 0

while guess != secret_number:
    guess = int(input('Guess the number (1-5): '))
    if guess != secret_number:
        print('Wrong! Try again.')

print('You got it!')

print('\nEjemplo de break:')
developer_name = ['Jess', 'Naomi', 'Tom']
print(f'Lista inicial: {developer_name}')

for developer in developer_name:
    if developer == 'Naomi':
        break # break se utiliza para detener la ejecución de un bucle
    print(developer)

print('\nEjemplo de continue:')
developer_name = ['Jess', 'Naomi', 'Tom']
print(f'Lista inicial: {developer_name}')

for developer in developer_name:
    if developer == 'Naomi':
        continue # continue se utiliza para omitir la iteración actual de un bucle y pasar a la siguiente iteración
    print(developer)

print('\nEjemplo de usar else en for y while:')
words = ['sky', 'apple', 'rhythm', 'fly', 'orange']
print(f'Lista inicial: {words}')

print('\nEjemplo:')
for word in words:
    for letter in word:
        if letter.lower() in 'aeiou':
            print(f"'{word}' contains the vowel '{letter}'")
            break
    else:
        print(f"'{word}' has no vowels")
