def calc_y_max(min_target_y):
    y, vy = 0, -min_target_y - 1
    while True:
        y += vy
        vy -= 1
        if vy == 0: # Maximum found
            return y

def x_start_min():
    x, vx = 0, 0
    while x < min(target_x):
        vx += 1
        x += vx
    return x, vx


def x_pos(vx_start):
    x, vx, t = 0, vx_start, 0
    while True:
        yield x, t
        t += 1
        x += vx
        vx = max(vx - 1, 0)


def y_pos(vy_start):
    y, vy, t = 0, vy_start, 0
    while True:
        yield y, t
        t += 1
        y += vy
        vy -= 1


target_x, target_y = [195, 238], [-93, -67]           # Puzzle input
# target_x, target_y = [20, 30], [-10, -5]            # Given Example
x_min, x_max, y_min, y_max = min(target_x), max(target_x), min(target_y), max(target_y)

print(f'The answer to part 1 = {calc_y_max(min(target_y))}')

range_vx = [x_start_min()[1], max(target_x)]
range_vy = [min(target_y), -min(target_y) - 1]

print(f'range vx = {range_vx} and range vy = {range_vy}')

time_table_x = dict()
for vx_start in range(range_vx[0], range_vx[1] + 1):
    gen_x = x_pos(vx_start)
    print(f'-- vx_start = {vx_start} --')
    time_table_x[vx_start] = []
    while True:
        val = next(gen_x)
        print(val)
        if x_min <= val[0] <= x_max:
            time_table_x[vx_start].append(val[1])
        elif val[0] > x_max:
            break
        if val[1] > x_max:
            break
    print(time_table_x[vx_start])
    if len(time_table_x[vx_start]) == 0:
        del time_table_x[vx_start]

# exit()

time_table_y = dict()
for vy_start in range(range_vy[0], range_vy[1] + 1):
    gen_y = y_pos(vy_start)
    print(f'-- vy_start = {vy_start} --')
    time_table_y[vy_start] = []
    while True:
        val = next(gen_y)
        print(val)
        if y_min <= val[0] <= y_max:
            time_table_y[vy_start].append(val[1])
        elif val[0] < y_min:
            break
        if val[1] > x_max:
            break
    print(time_table_y[vy_start])
    if len(time_table_y[vy_start]) == 0:
        del time_table_y[vy_start]

answer_part_2 = 0
for times_x in time_table_x.values():
    for times_y in time_table_y.values():
        for tx in times_x:
            if tx in times_y:
                answer_part_2 += 1
                break                   # Requitred --> some trajectories might pass twice but count only once
print(f'The answer to part 2 = {answer_part_2}')

