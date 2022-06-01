def operate(operator, *args):
    def add(*args):
        return sum(args)

    def subtract(x, *args):
        return x + sum(-k for k in args)

    def multiply(*args):
        result = 1

        for item in args:
            result *= item

        return result

    def divide(x, *args):
        result = x

        for item in args:
            result /= item

        return result

    if operator == '+':
        return add(*args)
    elif operator == '-':
        return subtract(*args)
    elif operator == '*':
        return multiply(*args)
    elif operator == '/':
        return divide(*args)


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
