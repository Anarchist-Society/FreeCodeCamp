my_str_1 = 'Hello'
my_str_2 = "World"

my_str_3 = """Multiline
string"""
my_str_4 = '''Another
miltiline
string'''

msg = "It's a sunny day"
quote = 'She said, "Hello World!"'

msg = 'It\'s a sunny day'
quote = "She said, \"Hello!\""

my_str = 'Hello World'
print(my_str)
print('Hello' in my_str) # True
print('hey' in my_str) # False
print('hi' in my_str) # False
print('e' in my_str) # true
print('f' in my_str) # False

print(len(my_str)) # 11
print(my_str[0])
print(my_str[1])
print(my_str[-1])
print(my_str[-2])

# Strings are immutable data types in Python. This means that you can reassign a different string to a variable:
greeting = 'hi'
greeting = 'hello'
print(greeting) # hello

# But direct modification of a string isn't allowed:
greeting = 'hi'
# greeting[0] = 'H' # TypeError: 'str' object does not support item assignment
