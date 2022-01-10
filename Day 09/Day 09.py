from termcolor import colored

with open('input.txt') as f:
    lines = f.read().splitlines()

print_part_1 = False
print_part_2 = False

grid = []
grid.append([9] * (len(lines[0]) + 2))
for line in lines:
    grid.append([9] + list(map(int, list(line))) + [9])
grid.append([9] * (len(lines[0]) + 2))

deltas = [-1, 1]
coords = []
answer_part_1 = 0

for y in range(1, len(grid) - 1):
    for x in range(1, len(grid[0]) - 1):
        low = True
        val = grid[y][x]
        for delta in deltas:
            if val >= grid[y + delta][x]:
                low = False
            if val >= grid[y][x + delta]:
                low = False
        if low:
            coord = (x, y)
            coords.append(coord)
            answer_part_1 += 1 + val

if print_part_1:
    print('--- GRID PART 1 ---')
    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[0]) - 1):
            color = 'blue'
            if (x, y) in coords:
                color = 'yellow'
            print(colored(grid[y][x], color), end='')
        print('')

print(f'The answer to part 1 = {answer_part_1}')

basins = []
basin_lengths = []

for coord in coords:
    temp_coords = [coord]
    finished_coords = []
    while len(temp_coords) != 0:
        cur_coord = temp_coords.pop()
        x, y = cur_coord[0], cur_coord[1]
        for delta in deltas:
            dx, dy = x + delta, y + delta
            if grid[y][x] <= grid[dy][x] < 9:
                new_coord = (x, dy)
                if new_coord not in temp_coords and new_coord not in finished_coords:
                    temp_coords.append(new_coord)
            if grid[y][x] <= grid[y][dx] < 9:
                new_coord = (dx, y)
                if new_coord not in temp_coords and new_coord not in finished_coords:
                    temp_coords.append(new_coord)
        finished_coords.append(cur_coord)
    basins.append(finished_coords.copy())
    basin_lengths.append(len(finished_coords))

basin_lengths.sort(reverse=True)
answer_part_2 = 1
for i in range(3):
    answer_part_2 *= basin_lengths[i]

if print_part_2:
    print('--- GRID PART 2 ---')
    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[0]) - 1):
            color = 'blue'
            coord = (x, y)
            if any(coord in sl for sl in basins):
                color = 'yellow'
            if coord in coords:
                color = 'red'
            print(colored(grid[y][x], color), end='')
        print('')
print(f'The answer to part 2 = {answer_part_2}')
