def age_assignment(*args, **kwargs):
    result = []

    for item in args:
        age = kwargs[item[0]]
        result.append(f'{item} is {age} years old.')

    return '\n'.join(sorted(result))


print(age_assignment("Peter", "George", G=26, P=19))
