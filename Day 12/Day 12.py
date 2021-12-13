with open('input.txt') as f:
    lines = f.read().splitlines()

paths, lower_caves = dict(), set()

for line in lines:
    val1, val2 = line.split('-')[0], line.split('-')[1]
    if val1 not in paths:
        paths[val1] = [val2]
    else:
        paths[val1].append(val2)
    if val2 not in paths:
        paths[val2] = [val1]
    else:
        paths[val2].append(val1)
    if val1 == val1.lower():
        lower_caves.add(val1)
    if val2 == val2.lower():
        lower_caves.add(val2)

unfinished_paths = [['start']]
finished_paths = []

while len(unfinished_paths) != 0:
    cur_path = unfinished_paths.pop(0)
    next_steps = paths[cur_path[-1]]
    for next_step in next_steps:
        if next_step == 'end':
            finished_paths.append(cur_path + [next_step])
            continue
        # if len(cur_path) > 1:
        #     if cur_path[-2] == next_step:
        #         continue                        # Do not directly backtrack
        if next_step in lower_caves:
            if cur_path.count(next_step) > 0:
                continue                        # Do not visit lower caves twice
        unfinished_paths.append(cur_path + [next_step])

print(f'Part 1: There are a total of {len(finished_paths)} paths possible')

unfinished_paths = [['start']]
finished_paths = []

while len(unfinished_paths) != 0:
    cur_path = unfinished_paths.pop(0)
    next_steps = paths[cur_path[-1]]
    for next_step in next_steps:
        if next_step == 'end':
            finished_paths.append(cur_path + [next_step])
            continue
        if next_step == 'start':
            continue                            # Do not return to start
        if next_step in lower_caves:
            already_two = False
            for lower_cave in lower_caves:
                if cur_path.count(lower_cave) == 2:
                    already_two = True
                    break
            if already_two:
                if cur_path.count(next_step) > 0:
                    continue                    # Do not visit lower caves twice
            else:
                if cur_path.count(next_step) > 1:
                    continue                    # Do not visit lower caves three times
        unfinished_paths.append(cur_path + [next_step])

print(f'Part 2: There are a total of {len(finished_paths)} paths possible')
