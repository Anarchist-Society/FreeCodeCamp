print('What Are String Concatenation and String Interpolation?\n')

my_str_1 = 'Hello'
my_str_2 = "World"

str_plus_str = my_str_1 + ' ' + my_str_2
print(str_plus_str) # Hello World

# But note that this only works with strings. If you try to concatenate a string with a number, you'll get a TypeError:
name = 'John Doe'
age = 26

# name_and_age = name + age
# print(name_and_age) # TypeError: can only concatenate str (not "int") to str

# This happens because Python does not automatically convert other data types like integers into strings when you concatenate them. Python requires all elements to be strings before it can concatenate them. To fix that, you can convert the number into a string with the built-in str() function, which returns the string representation of the given object without modifying the original object:

name_and_age = name + str(age)
print(name_and_age) # John Doe26

# You can also use the augmented assignment operator for concatenation. This is represented by a plus and equals sign (+=), and performs both concatenation and assignment in one step. Here's it in action:
name = 'John Doe'
age = 26

name_and_age = name  # Start with the name
name_and_age += str(age)  # Append the age as string

print(name_and_age)  # John Doe26

# String Interpolation
name = 'John Doe'
age = 26
name_and_age = f'My name is {name} and I am {age} years old'
print(name_and_age) # My name is John Doe and I am 26 years old

num1 = 5
num2 = 10
print(f'The sum of {num1} and {num2} is {num1 + num2}') # The sum of 5 and 10 is 15
