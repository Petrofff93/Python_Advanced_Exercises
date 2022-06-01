def multiply(*args):
    result = 1

    for x in args:
        result *= x

    return result


print(multiply(1, 2, 3, 4))
