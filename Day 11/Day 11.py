with open('input.txt') as f:
    lines = f.read().splitlines()


def flash(coord):
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            if dy == dx == 0:                          # Do not account for current coordinate
                continue
            target = (coord[0] + dx, coord[1] + dy)
            if grid[target[1]][target[0]] == -1:       # Skip fictive boundary -1 elements
                continue
            else:
                grid[target[1]][target[0]] += 1
                if grid[target[1]][target[0]] > 9 and target not in flash_coords and target not in flash_finished:
                    flash_coords.append(target)


grid, target_grid = [], []
grid.append([-1] * 12), target_grid.append([-1] * 12)    # Add boundary of -1's to deal with boundary conditions
for line in lines:
    grid.append([-1] + list(map(int, line)) + [-1]), target_grid.append([-1] + [0] * 10 + [-1])
grid.append([-1] * 12), target_grid.append([-1] * 12)

steps = 100
flashes = 0
step = 0

while True:
    step += 1
    flash_coords = []
    flash_finished = []
    for y in range(1, 11):        # First add 1 to all position (excluding boundary -1's)
        for x in range(1, 11):
            coord = (x, y)
            grid[y][x] += 1
            if grid[y][x] > 9:    # Keep track of coords that want to flash this step
                flash_coords.append(coord)
    while len(flash_coords) > 0:  # Flassh every point in flash_coords
        cur_coord = flash_coords.pop()
        flash_finished.append(cur_coord)
        flash(cur_coord)
    for coord in flash_finished:  # Reset every flashed coord to 0
        grid[coord[1]][coord[0]] = 0
    flashes += len(flash_finished)
    if step == 100:
        print(f'The answer to part 1 = There are a total of {flashes} flashes after {step} steps')
    if grid == target_grid:
        print(f'THe answer to part 2 = THe first step all octopuses flashes simultaniously is step {step}')
        break
