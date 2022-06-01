def get_info(name, town, age):
    return f'This is {name} from {town} and he is {age} years old'


person_info = {
    'name': 'George',
    'town': 'Vratsa',
    'age': 29
}

print(get_info(**person_info))
