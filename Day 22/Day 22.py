import numpy as np

with open('input.txt') as f:
    lines = f.read().splitlines()

x_min, y_min, z_min = -50, -50, -50
x_max, y_max, z_max = 50, 50, 50

grid = np.zeros((x_max - x_min + 1, y_max - y_min + 1, z_max - z_min + 1), int)  # All entries including 0
print(np.shape(grid))
step = 0
for line in lines:
    step += 1
    x_start, x_end = int(line.split('=')[1].split('.')[0]) - x_min, x_max + int(line.split('..')[1].split(',')[0])
    y_start, y_end = int(line.split('=')[2].split('.')[0]) - y_min, y_max + int(line.split('..')[2].split(',')[0])
    z_start, z_end = int(line.split('=')[3].split('.')[0]) - z_min, z_max + int(line.split('..')[3])
    if x_end < 0 or y_end < 0 or z_end < 0 or x_start > x_max - x_min or y_start > y_max - y_min or z_start > z_max - z_min:
        # Area out of bounds
        print(f'step {step} is out of bound and passed')
    else:
        x_start, x_end = max(x_start, 0), min(x_end, x_max - x_min)
        y_start, y_end = max(y_start, 0), min(y_end, y_max - y_min)
        z_start, z_end = max(z_start, 0), min(z_end, z_max - z_min)
        print(f'x_start = {x_start}, x_end = {x_end}')
        print(f'x_start = {y_start}, x_end = {y_end}')
        print(f'x_start = {z_start}, x_end = {z_end}')
        sg = grid[x_start: x_end + 1, y_start:y_end + 1, z_start:z_end + 1]
        if 'on' in line:
            sg[sg == 0] = 1
        elif 'off' in line:
            sg[sg == 1] = 0
    print(f'There are {np.count_nonzero(grid == 1)} cubes on after step {step}')

cubes_on = np.count_nonzero(grid == 1)

print(f'The answer to part 1 = {cubes_on}')

# Example
# sub_array = grid[:10, :10, :10]
# sub_array[sub_array == 0] = 1
# print(grid)
