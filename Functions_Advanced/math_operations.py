from collections import deque


def math_operations(*args, **kwargs):
    numbers = deque(args)

    while numbers:
        add = numbers.popleft()
        kwargs['a'] += add

        if not numbers:
            break

        subtract = numbers.popleft()
        kwargs['s'] -= subtract

        if not numbers:
            break

        divide = numbers.popleft()
        if divide != 0:
            kwargs['d'] /= divide

        if not numbers:
            break

        multiply = numbers.popleft()
        kwargs['m'] *= multiply

    result = [f'{key}: {value:.01f}' for key, value in sorted(kwargs.items(), key=lambda x: ((-x[1]), x[0]))]
    return '\n'.join(result)


print(math_operations(6.0, a=0, s=0, d=5, m=0))
