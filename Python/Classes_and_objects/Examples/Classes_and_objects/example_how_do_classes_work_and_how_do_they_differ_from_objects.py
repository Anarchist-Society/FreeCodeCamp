print('How Do Classes Work and How Do They Differ From Objects?\n')

print('Example 1:')

class ClassName:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def sample_method(self):
        print(self.name.upper())

print('Example 2')

class Dog:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def bark(self):
        print(f'{self.name.upper()} says woof woof!')

dog_1 = Dog('Jack', 3)
dog_2 = Dog('Thatcher', 5)

# Call the bark method
dog_1.bark() # JACK says woof woof! I'm 3 years old!
dog_2.bark() # THATCHER says woof woof! I'm 5 years old!
