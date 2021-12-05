with open('input.txt') as f:
    lines = f.read().splitlines()

points = []

for line in lines:
    point = list()  # x1, y1, x2, y2
    point.append(int(line.split(',')[0]))
    point.append(int(line.split(',')[1].split(' ')[0]))
    point.append(int(line.split(' ')[2].split(',')[0]))
    point.append(int(line.split(',')[-1]))
    points.append(point)

x_max = max(max(map(lambda x: x[0], points)) + 1, max(map(lambda x: x[2], points)) + 1)
y_max = max(max(map(lambda y: y[1], points)) + 1, max(map(lambda y: y[3], points)) + 1)

grid = []
for y in range(y_max):
    grid.append([0] * x_max)

answer_part_1 = 0

for point in points:
    if point[0] == point[2]:  # vertical line
        x = point[0]
        p1 = min(point[1], point[3])
        p2 = max(point[1], point[3]) + 1
        for y in range(p1, p2):
            grid[y][x] += 1
            if grid[y][x] == 2:
                answer_part_1 += 1
    elif point[1] == point[3]:  # horizontal line
        y = point[1]
        p1 = min(point[0], point[2])
        p2 = max(point[0], point[2]) + 1
        for x in range(p1, p2):
            grid[y][x] += 1
            if grid[y][x] == 2:
                answer_part_1 += 1

print(f'The answer to part 1: {answer_part_1} points overlap')

for point in points:
    if point[0] != point[2] and point[1] != point[3]:  #  diagonal line
        if point[0] < point[2]:
            factor_x = 1
        else:
            factor_x = -1
        if point[1] < point[3]:
            factor_y = 1
        else:
            factor_y = -1
        for step in range(abs(point[0] - point[2]) + 1):
            x = point[0] + step * factor_x
            y = point[1] + step * factor_y
            grid[y][x] += 1
            if grid[y][x] == 2:
                answer_part_1 += 1

print(f'The answer to part 2: {answer_part_1} points overlap')
