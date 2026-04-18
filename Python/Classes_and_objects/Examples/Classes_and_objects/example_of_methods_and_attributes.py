print('What Are Methods and Attributes, and How Do They Work?\n')

print('Example 1:\n')
class Dog_01:
    species = 'French Bulldog' # Class attribute
    def __init__(self, name):
        self.name = name # Instance attribute

print(Dog_01.species) # French Bulldog

dog1 = Dog_01('Jack')
print(dog1.name) # Jack
print(dog1.species) # French Bulldog

dog2 = Dog_01('Tom')
print(dog2.name) # Tom
print(dog2.species) # French Bulldog

print('Example 2:\n')

class Car_01:
    def __init__(self, color, model) -> None:
        self.color = color
        self.model = model

car_1 = Car_01("red", "Toyota Corolla")
car_2 = Car_01("green", "Lamborghini Revuelto")

print(car_1.model) # Toyota Corolla
print(car_2.model) # Lamborghini Revuelto

print(car_1.color) # red
print(car_2.color) # green

print('Example 3: \n')
class Dog_02:
    species = 'French Bulldog'

    def __init__(self, name) -> None:
        self.name = name

    def bark(self):
        return f'{self.name} says woof woof!'

jack = Dog_02('Jack')
jill = Dog_02('Jill')

print(jack.bark()) # Jack says woof woof!
print(jill.bark()) # Jill says woof woof!

class Car:
    def __init__(self, color, model) -> None:
        self.color = color # Instance attribute
        self.model = model # Instance attribute

    def describe(self):
        return f'This car is a {self.color} {self.model}'

car_1 = Car("red", "Toyota Corolla")
car_2 = Car("green", "Lamborghini Revuelto")

print(car_1.describe()) # This car is a red Toyota Corolla
print(car_2.describe()) # This car is a green Lamborghini Revuelto
