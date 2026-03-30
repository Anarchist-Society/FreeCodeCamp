print('How Do Functions Work in Python?\n')

name = input('What is your name?: ') # User types "Kolade" and presses Enter
print('Hello',name) # Output: Hello Kolade

# On the other hand, int() converts a number, boolean, and a numeric string into an integer:
print(int(3.14)) # 3
print(int('42')) # 42
print(int(True)) # 1
print(int(False)) # 0

def hello():
    print('Hello World')

hello()

def calculate_sum_01(a,b):
    print(a + b)

calculate_sum_01(3,1) # 4

def calculate_sum_02(a,b):
    return a + b

my_sum = calculate_sum_02(3,1)
print(my_sum)
