print('Build a Number Pattern Generator:\n')

def number_pattern(n):
    if not isinstance(n, int):
        return 'Argument must be an integer value.'

    if n < 1:
        return 'Argument must be an integer greater than 0.'

    result = ''
    n += 1
    for i in range(1, n):
        if i == n - 1:
            result += str(i)
        else:
            result += str(i) + ' '
    return result

print(number_pattern(4))
print(number_pattern(12))
