print('What Is Scope in Python and How Does It Work?\n')

# What Is Scope in Python and How Does It Work?

# Local scope means that a variable declared inside a function or class can only be accessed within that function or class.
def my_func():
    my_var = 10
    print(my_var)

# Enclosing scope means that a function that's nested inside another function can access the variables of the function it's nested within.
def outer_func_01():
    msg = 'Hello there!'

    def inner_func_01():
        print(msg)

    inner_func_01()

outer_func_01()

def outer_func_02():
    msg = 'Hello there!'
    res = "" # Declare res in the enclosing scope

    def inner_func_02():
        nonlocal res
        res = 'How are you?'
        print(msg)

    inner_func_02()
    print(res)

outer_func_02()

# Output:
# Hello there!
# How are you?

# Global scope refers to variables that are declared outside any functions or classes which can be accessed from anywhere in the program. Here, my_var can be accessed anywhere, even inside a function it's not defined in:
my_var = 100

def show_var():
    print(my_var)

show_var() # 100
print(my_var) # 100

# And if you want to make a locally scoped variable defined inside a function globally accessible, you can use the global keyword:
my_var_1 = 7

def show_vars():
    global my_var_2
    my_var_2 = 10
    print(my_var_1)
    print(my_var_2)

show_var() # 7 10

# my_var_2 is now a global variable and can be accessed anywhere in the program
print(my_var_2) # 10

# You can also use the global keyword to modify a global variable:
my_var = 10  # A global variable

def change_var():
    global my_var  # Allows modification of a global variable
    my_var = 20

change_var()

print(my_var)  # my_var is now modified globally to 20

# Finally, built-in scope refers to all of Python's built-in functions, modules, and keywords, and are available anywhere in your program:
print(str(45)) # '45'
print(type(3.14)) # <class 'float'>
print(isinstance(3, str)) # False
