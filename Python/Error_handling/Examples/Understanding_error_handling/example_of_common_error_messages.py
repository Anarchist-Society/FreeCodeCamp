print('What Are Some Common Error Messages in Python?\n')

print('Example of SyntaxError:\n')
print('''
print("Hello, world!" -> # SyntaxError: unexpected EOF while parsing
''')

print('Example of NameError:\n')
print('''
print(name) -> NameError: name 'name' is not defined
''')

print('Example of TypeError:\n')
print('''
5 + "5" -> TypeError: unsupported operand type(s) for +: 'int' and 'str'
''')

print('Example of IndexError:\n')
print('''
my_list = [1, 2, 3]
print(my_list[5]) -> IndexError: list index out of range
''')

print('AttributeError:\n')
print('''
num = 42
num.append(5)
# AttributeError: 'int' object has no attribute 'append'
''')
