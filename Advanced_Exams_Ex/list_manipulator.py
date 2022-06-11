def list_manipulator(*args):
    current_list = args[0]

    first_command = args[1]
    second_command = args[2]

    numbers = [int(x) for x in args[3:]]
    if numbers:
        if first_command == 'add' and second_command == 'beginning':
            current_list = numbers + current_list
            return current_list

        elif first_command == 'add' and second_command == 'end':
            for num in numbers:
                current_list.append(num)
            return current_list

        elif first_command == 'remove' and second_command == 'end':
            num = numbers[0]
            current_list = current_list[0:-num]
            return current_list

        elif first_command == 'remove' and second_command == 'beginning':
            num = numbers[0]
            current_list = current_list[num:]
            return current_list

    else:
        if first_command == 'remove' and second_command == 'end':
            current_list = current_list[0:-1]
            return current_list

        elif first_command == 'remove' and second_command == 'beginning':
            current_list = current_list[1:]
            return current_list
