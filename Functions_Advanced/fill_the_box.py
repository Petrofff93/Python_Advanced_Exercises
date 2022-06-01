def fill_the_box(height, lenght, width, *args):
    box_size = height * lenght * width
    cubes = 0

    for cube in args:
        if cube == 'Finish':
            break

        if box_size >= cube:
            box_size -= cube
        else:
            cube -= box_size
            cubes += cube
            box_size = 0

    if box_size:
        return f'There is free space in the box. You could put {box_size} more cubes.'
    else:
        return f'No more free space! You have {cubes} more cubes.'


print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))