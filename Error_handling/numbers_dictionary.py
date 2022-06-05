numbers_dictionary = {}

line = input('Please enter the value as string (eg. one, two, three.. ) ')

while line != "Search":
    number_as_string = line
    try:
        number = int(input('Please enter the number as integer (eg. 1,2,3.. ) '))
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print('The value is not integer! Please provide an integer')
        continue

    line = input('Please enter the value as string (eg one, two, three.. ) ')

line = input('Please enter the searched value as string (eg. one, two, three.. ) ')
while line != "Remove":
    try:
        searched = line
        print(numbers_dictionary[searched])
    except TypeError:
        print('Please provide the searched number as string!')
    except KeyError:
        print('The searched number is not in the list (or you provided integer instead of string)!')

    line = input('Please enter the searched value as string (eg. one, two, three.. ) ')

line = input('Please provide the number (as string) which you want to remove ')

while line != "End":
    try:
        searched = line
        del numbers_dictionary[searched]
    except KeyError:
        print('The number which you want to remove, does not exists!')
    line = input('Please provide the string which you want to remove ')

print(numbers_dictionary)
