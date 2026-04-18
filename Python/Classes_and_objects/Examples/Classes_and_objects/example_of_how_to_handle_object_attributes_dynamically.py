print('How to Handle Object Attributes Dynamically?\n')

print('Example 1:\n')

class Car:
    def __init__(self, brand, model) -> None:
        self.brand = brand
        self.model = model

my_car = Car('Lamborghini', 'Gallardo')
print(my_car.brand) # Lamborghini
print(my_car.model) # Gallardo

print('\nExample of getattr():\n')
class Person_01:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

person = Person_01('John Doe', 30)

print(getattr(person, 'name')) # John Doe
print(getattr(person, 'age')) # 30
print(getattr(person, 'city', 'Milano')) # Milano

attr_name = input('\nEnter the attribute you want to see: ')
print(getattr(person, attr_name, 'Attribute not found'))

print('\nExample of dir():\n')
# Loop through all attributes of the person object with dir() function
for attr in dir(person):
    # Ignore dunder methods like __init__ or __str__ and regular methods
    if not attr.startswith('__') and not callable(getattr(person, attr)):
        value = getattr(person, attr)
        print(f'{attr}: {value}')

# Output
# age: 30
# name: John Doe

print('\nExample of setattr():\n')

class Configuration:
    pass

# Data loaded at runtime (like from a config or env file)
settings_data = {
    'server_url': 'https://api.example.com',
    'timeout_sec': 30,
    'max_retries': 5
}

config_obj = Configuration()

# Dynamically set attributes using dictionary keys and values
for attr_name, attr_value in settings_data.items():
    setattr(config_obj, attr_name, attr_value)

print(config_obj.server_url) # https://api.example.com
print(config_obj.timeout_sec) # 30

print('\nExample of hasattr():\n')

class Product:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

product_a = Product('T-Shirt', 25)

required_attributes = ['name', 'price', 'inventory_id']

for attr in required_attributes:
    if not hasattr(product_a, attr):
        print(f"ERROR: Product is missing the required attribute: '{attr}'")
    else:
        # Access the attributes dynamically once their existence is confirmed
        print(f'{attr}: {getattr(product_a, attr)}')

# Output:
# name: T-Shirt
# price: 25
# ERROR: Product is missing the required attribute: 'inventory_id'

print('\nExample of delattr():\n')

class UserSession:
    def __init__(self, user_id, token) -> None:
        self.user_id = user_id
        self.token = token # sensitive
        self.temp_counter = 0 # temporary

session = UserSession(101, 'a1b2c3d4e5')

# List of attributes to remove dynamically before "saving" the session
attributes_to_clean = ['auth_token', 'temp_counter']

# Dynamically remove specified attributes
for attr in attributes_to_clean:
    if hasattr(session, attr):
        delattr(session, attr)
        print(f'Removed attribute')

print('\nFinal attributes remaining:')

# Loop through the remaining attributes with dir()
for attr in dir(session):
    # Ignore dunder methods like __init__ or __str__ and regular methods
    if not attr.startswith('__'):
        print(f' - {attr}: {getattr(session, attr)}')

# Output:
# Removed attribute: auth_token
# Removed attribute: temp_counter

# Final attributes remaining:
#  - user_id: 101
