# Функции: задание 1

def get_sum(one, two, delimiter='&'):
    one = str(one)
    two = str(two)
    delimiter = str('&')
    return str(one + delimiter + two)


result = get_sum('Learn', 'python').upper()
print(result)


