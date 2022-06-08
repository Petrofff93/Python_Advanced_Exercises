from os.path import exists

while True:
    line = input().split('-')

    if line[0] == 'End':
        break

    command = line[0]
    file_and_extension = line[1]

    if command == 'Create':
        with open(f'{file_and_extension}', 'w') as file:
            pass

    elif command == 'Add':
        with open(f'{file_and_extension}', 'a+') as file:
            file.write(f'{line[-1]}\n')

    elif command == 'Replace':
        if exists(file_and_extension):
            old_string = line[2]
            new_string = line[3]
            current_text = ''
            with open(file_and_extension, 'r') as file:
                for row in file:
                    current_text += row
                current_text = current_text.replace(old_string, new_string)
            with open(file_and_extension, 'w+') as file:
                file.write(current_text)

        else:
            print('An error occurred')

    elif command == 'Delete':
        if exists(file_and_extension):
            del file_and_extension
        else:
            print('An error occurred')







