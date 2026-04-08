print('What Are Dictionaries, and How Do They Work?\n')

print('Example of dictionary:')
pizza = {
    'name': 'Margherita Pizza',
    'price': 8.9,
    'calories_per_slice': 250,
    'toppings': ['mozzarella', 'basil']
}

print('\nExample of dictionary 2:')
pizza = dict([('name', 'Margherita Pizza'), ('price', 8.9), ('calories_per_slice', 250), ('toppings', ['mozzarella', 'basil'])])
print(f'Nombre de la pizza: {pizza['name']}')
print(f'Precio de la pizza: {pizza['price']}')

print('\nEjemplo de usar el método get():')
print(f'Toopings de la pizza: {pizza.get('toppings')}')

print('\nEjemplo de usar el método keys():')
print(f'Esto devuelve las claves del diccionario: {pizza.keys()}')

print('\nEjemplo de usar el método values():')
print(f'Esto devuelve los valores del diccionario: {pizza.values()}')

print('\nEjemplo de usar el método items():')
print(f'Esto devuelve una vista del diccionario: {pizza.items()}')

print('\nEjemplo de usar el método clear():')
print(f'Esto elimina todas las claves y valores del diccionario: {pizza.clear()}')
print(f'Diccionario: {pizza}')

pizza = {
    'name': 'Margherita Pizza',
    'price': 8.9,
    'calories_per_slice': 250,
    'toppings': ['mozzarella', 'basil']
}

print('\nEjemplo de usar el método pop():')
print(f'Diccionario pizza antes: {pizza}')
print(f'Este método elimina la clave y el valor, se le pasa la clave como argumento, si la clave no existe devuelve el segundo valor que se le pasa como argumento: {pizza.pop('price', 10)}')
print('Si la clave no existe y no se le pasa un segundo argumento devuelve error: KeyError')
print(f'Diccionario pizza después: {pizza}')

print('\nEjemplo de usar el método popitem():')
pizza = {
    'name': 'Margherita Pizza',
    'price': 8.9,
    'calories_per_slice': 250,
    'toppings': ['mozzarella', 'basil']
}
print(f'Diccionario pizza antes: {pizza}')
print(f'Este método elimina el último valor del diccionario: {pizza.popitem()}')
print(f'Diccionario pizza después: {pizza}')

print('\nEjemplo de usar update():')
pizza = {
    'name': 'Margherita Pizza',
    'price': 8.9,
    'calories_per_slice': 250,
    'toppings': ['mozzarella', 'basil']
}

print(f'Diccionario pizza antes: {pizza}')
print(f'Este método actualiza los valores en función de sus claves: {pizza.update({'price': 15, 'total_time': 25})}')
print(f'Diccionario pizza después: {pizza}')
