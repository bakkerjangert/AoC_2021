with open('input.txt') as f:
    lines = f.read().splitlines()

index_string = lines[0]

print(f'Testing 3 x 3 dots: {index_string[int("0" * 9, 2)]}')
print(f'Testing 3 x 3 hashtags : {index_string[int("1" * 9, 2)]}')

grid = []
for i in range(2):
    grid.append('.' * (len(lines[2]) + 4))
for line in lines[2:]:
    grid.append('.' * 2 + line + '.' * 2)
for i in range(2):
    grid.append('.' * (len(lines[2]) + 4))

steps = 50
new_grid = None

for step in range(steps):
    new_grid = []
    x_start, x_end = 1, len(grid[0]) - 1
    y_start, y_end = 1, len(grid) - 1
    for y in range(y_start, y_end):
        new_grid.append('')
        for x in range(x_start, x_end):
            string = grid[y - 1][x - 1: x + 2] + grid[y][x - 1: x + 2] + grid[y + 1][x - 1: x + 2]
            bin_number = string.replace('.', '0').replace('#', '1')
            # print(bin_number)
            new_grid[-1] += index_string[int(bin_number, 2)]
    grid = []
    if step % 2 == 0:
        char = '#'
    else:
        char = '.'
    for i in range(2):
        grid.append(char * (len(new_grid[0]) + 4))
    for line in new_grid:
        grid.append(char * 2 + line + char * 2)
    for i in range(2):
        grid.append(char * (len(new_grid) + 4))
    # for line in grid:
    #     print(line)
    if step == 1:
        answer_part_1 = 0
        for line in grid:
            answer_part_1 += line.count('#')
            print(line)
        print(f'The answer to part 1 = {answer_part_1}')

answer_part_2 = 0
for line in grid:
    answer_part_2 += line.count('#')
    print(line)
print(f'The answer to part 2 = {answer_part_2}')
