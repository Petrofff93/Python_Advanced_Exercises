def numbers_searching(*args):
    duplicates_list = []

    min_number = min(args)
    max_number = max(args)

    missing_number = 0

    for number in range(min_number, max_number, 1):
        if number not in args:
            missing_number = number
            break

    for num in args:
        if args.count(num) > 1:
            duplicates_list.append(num)

    return [missing_number, sorted(list(set(duplicates_list)))]


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))