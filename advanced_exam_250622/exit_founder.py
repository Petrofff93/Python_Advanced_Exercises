players = input().split(', ')
players_dict = {
    players[0]: 0,
    players[1]: 0
}

size = 6
matrix = []

for _ in range(size):
    matrix.append(input().split())

while True:
    current_player = players[0]
    if players_dict[current_player] == 1:
        coordinates = input().split(', ')
        row, col = int(coordinates[0][1:]), int(coordinates[1][0:-1])

        players[0], players[1] = players[1], players[0]
        players_dict[current_player] = 0
        continue

    coordinates = input().split(', ')
    row, col = int(coordinates[0][1:]), int(coordinates[1][0:-1])

    if matrix[row][col] == 'E':
        print(f"{current_player} found the Exit and wins the game!")
        break
    if matrix[row][col] == 'T':
        print(f"{current_player} is out of the game! The winner is {players[1]}.")
        break
    if matrix[row][col] == 'W':
        print(f"{current_player} hits a wall and needs to rest.")
        players_dict[current_player] += 1

    players[0], players[1] = players[1], players[0]
