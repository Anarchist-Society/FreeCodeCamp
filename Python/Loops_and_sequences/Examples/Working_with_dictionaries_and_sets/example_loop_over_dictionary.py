print('What Are Some Common Techniques to Loop Over a Dictionary?\n')

print('Ejemplo 1:')
products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}

print(f'Initial map: {products}')

print(f'\nProducts 1:')
for product in products.keys():
    print(product)

print(f'\nProducts 2:')
for product in products:
    print(product)

print(f'\nPrices:')
for price in products.values():
    print(price)

print(f'\nProducts and prices 1:')
for product in products.items():
    print(product)

print(f'\nProducts and prices 2:')
for product, price in products.items():
    print(f'{product}, {price}')

print('\nExample with 20% discount: ')
print(f'Initial map: {products}')
for product, price in products.items():
    products[product] = round(price * 0.8)
print(f'Map with discount: {products}')

print('\nExample 1 with enumerate:')
for product in enumerate(products):
    print(product)

print('\nExample 2 with enumerate:')
for index, product in enumerate(products):
    print(index, product)

print('\nExample 3 with enumerate:')
for price in enumerate(products):
    print(price)

print('\nExample 4 with enumerate:')
for index, price in enumerate(products):
    print(index, price)

print('\nExample 5 with enumerate:')
for index, product in enumerate(products.items()):
    print(index, product)

print('\nExample 6 with enumerate:')
for index, product in enumerate(products.items(), 1):
    print(index, product)
