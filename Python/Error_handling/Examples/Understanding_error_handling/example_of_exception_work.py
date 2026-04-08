print('How Does Exception Handling Work?\n')

print('Example 1:\n')

try: # try: The block of code where you anticipate an error might occur.
    x = 10 / 0
except ValueError:
    print('That was not a valid number.')
except ZeroDivisionError as e: # except: This block runs if an error of the specified type is raised inside the try.
    print("You can't divide by zero!")
    print(f'Error occurred: {e}')
else: # else: Runs if no exception is raised in the try block.
    print('Division successful:', x)
finally: # finally: Runs no matter what—whether or not an exception occurred. Useful for clean-up tasks like closing files or releasing resources.
    print('This block always runs.')
