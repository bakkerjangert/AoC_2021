from copy import deepcopy
with open('input.txt') as f:
    lines = f.read().splitlines()

grid = []
for line in lines:
    grid.append([])
    for char in line:
        grid[-1].append(char)

half_steps = 58 * 2
half_step = 0
while True:
    print(f'Analysing step {(half_step + 1) / 2}')
    if half_step % 2 == 0:
        cur_state = deepcopy(grid)
    new_grid = deepcopy(grid)
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if half_step % 2 == 0:  # move east
                if grid[y][x] == '>':
                    if x == len(grid[0]) - 1:
                        if grid[y][0] == '.':
                            # move
                            new_grid[y][x] = '.'
                            new_grid[y][0] = '>'
                    else:
                        if grid[y][x + 1] == '.':
                            new_grid[y][x] = '.'
                            new_grid[y][x + 1] = '>'
            elif half_step % 2 == 1:  # move south
                if grid[y][x] == 'v':
                    if y == len(grid) - 1:
                        if grid[0][x] == '.':
                            # move
                            new_grid[y][x] = '.'
                            new_grid[0][x] = 'v'
                    else:
                        if grid[y + 1][x] == '.':
                            new_grid[y][x] = '.'
                            new_grid[y + 1][x] = 'v'
    if half_step % 2 == 1:
        if grid == cur_state:
            print(f'Final state reached after {(half_step + 1) // 2} steps')
            break
    grid = deepcopy(new_grid)
    half_step += 1
    # if half_step % 2 == 1:
    #     print(f'--- State at step {(half_step + 1) // 2} ---')
    #     for line in grid:
    #         print(''.join(line))
    #     # input('Pause ...')