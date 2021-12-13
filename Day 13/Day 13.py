from termcolor import colored

with open('input.txt') as f:
    lines = f.read().splitlines()

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
            print(colored('$', color='yellow'), end='')
        else:
            print(' ', end='')
    print('')



