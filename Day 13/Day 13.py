from termcolor import colored
import turtle

with open('extreme2.txt') as f:
    lines = f.read().splitlines()

print_turtle = True

coords = []
instructions = []


def fold(direction, number):
    directions = {'x': 0, 'y': 1}
    fold_line = number
    val = directions[direction]
    for coord in coords:
        if coord[val] > fold_line:
            coord[val] = fold_line - (coord[val] - fold_line)
    return None


for line in lines:
    if ',' in line:
        coords.append(list(map(int, line.split(','))))
    elif 'fold' in line:
        instructions.append((line.split(' ')[-1].split('=')[0], int(line.split('=')[-1])))

boundaries = {'x': 0, 'y': 0}
first_fold = True

for instruction in instructions:
    fold(instruction[0], instruction[1])
    boundaries[instruction[0]] = instruction[1]
    if first_fold:
        tup_coords = map(tuple, coords)
        amount = len(set(tup_coords))
        print(f'Part 1: There are {amount} points visible after one fold')
        first_fold = False

print('\nPart 2:\n')
for y in range(boundaries['y']):
    for x in range(boundaries['x']):
        if [x, y] in coords:
            print(colored('@', color='yellow'), end='')
        else:
            print(' ', end='')
    print('')

# Turtle part 2
if print_turtle:
    scale = 4
    turtle.delay(0), turtle.hideturtle(), turtle.speed(7.5), turtle.tracer(0, 0), turtle.color('black'), turtle.width(0.7 * scale)
    delta_x, delta_y = -max(coords, key=lambda x: x[0])[0] // 2,  -max(coords, key=lambda x: x[1])[1] // 2

    for x in range(boundaries['x']):
        for y in range(boundaries['y']):
            if [x, y] in coords:
                for dx in (-1, 0, 1):
                    for dy in (-1, 0, 1):
                        if dx == dy == 0:       # Skip current point
                            continue
                        if [x + dx, y + dy] in coords:
                            turtle.up(), turtle.goto((x + delta_x) * scale, -(y + delta_y) * scale)
                            turtle.down(), turtle.goto(((x + delta_x) + dx) * scale, -((y + delta_y) + dy) * scale)
    turtle.Screen().update(), turtle.done()
