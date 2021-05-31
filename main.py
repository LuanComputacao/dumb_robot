import sys

directions = ['N', 'E', 'S', 'W']
x_lim = 5
y_lim = 5

vertical = {
    'N': 1,
    'S': -1,
}

horizontal = {
    'E': 1,
    'W': -1,
}


def rotate(coordinates: tuple, direction: str):
    direction = direction.upper()

    pos = directions.index(coordinates[-1])
    pos = pos - 1 if direction == 'L' else pos + 1

    if direction == 'L':
        return coordinates[0], coordinates[1], directions[pos]

    return \
        coordinates[0],\
        coordinates[1], \
        directions[pos if pos <= 3 else pos - 4]


def move(coordinates: tuple):
    x, y, direction = coordinates

    if direction in vertical.keys():
        y += vertical[direction]
    else:
        x += horizontal[direction]

    return \
        0 if x < 0 else x_lim if x > x_lim else x, \
        0 if y < 0 else y_lim if y > y_lim else y, \
        direction


def main(command_list: list, coordinates: tuple):
    for command in command_list:
        if command in ['L', 'R']:
            coordinates = rotate(coordinates, command)
        else:
            coordinates = move(coordinates)

    return coordinates


if __name__ == '__main__':
    commands = sys.argv[1]

    coordinates = sys.argv[2][1:-1].split(',')
    coordinates = int(coordinates[0]), int(coordinates[1]), coordinates[2]

    new_coordinates = main(commands, coordinates)
    print(f'Previous coordinates: {coordinates}')
    print(f'Current coordinates: {new_coordinates}')
