my_integer_var = 10
print('Integer:',my_integer_var) # Integer: 10

my_float_var = 4.50
print('Float:',my_float_var) # Float: 4.5

my_string_var = 'hello'
print('String:',my_string_var) # String: hello

my_boolean_var = 'True'
print('Boolean:',my_boolean_var)

# Set: An unordered collection of unique elements
my_set_var = {7, 'hello', 8.5}
print('Set:', my_set_var) # Set: {7, 'hello', 8.5}

# Dictionary: A collection of key-value pairs enclosed in curly braces
my_dictionary_var = {'name':'Alice','age':'25'}
print('Dictionary:',my_dictionary_var) # Dictionary: {'name': 'Alice', 'age': 25}

# Tuple: An inmmutable ordered collection, enclosed in parentheses
my_tuple_var = (7, 'hello', 8.5)
print('Tuple:',my_tuple_var) # Tuple: (7, 'hello', 8.5)

my_range_var = range(5)
print('Range',my_range_var) # Range: range(0, 5)

# List: An ordered collection of elements that supports different data types.
my_list = [22,'hello world',3.14,True]
print(my_list) # [22, 'Hello world', 3.14, True]

my_none_var = None
print('None:',my_none_var) # None: None

# To get the data type of a variable, you can use the type() function:
my_var_1 = 'Hello world'
my_var_2 = 21
print(type(my_var_1))
print(type(my_var_2))

print(isinstance('Hello world',str)) # True
print(isinstance(True,bool)) # True
print(isinstance(42,int)) # True
print(isinstance('John Doe',int)) # False
