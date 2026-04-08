print('What Are Some Good Debugging Techniques in Python?\n')

print('Using the print function and f-strings:\n')
def add(a, b):
    result = a + b
    print(f'Adding {a} and {b} gives {result}')
    return result

print('Interactive Debugging with the pdb Module')

import pdb

def divide(a, b):
    pdb.set_trace()
    return a / b

print(divide(10, 2))

print('IDE Debugging Tools\n')

print('Using VS Code Debugger\n')
