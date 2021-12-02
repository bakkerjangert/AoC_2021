with open('input.txt') as f:
    lines = f.read().splitlines()

part_1 = {'depth': 0,
          'horizontal position': 0}

part_2 = {'depth': 0,
          'horizontal position': 0,
          'aim': 0}

for line in lines:
    if 'up' in line:
        part_1['depth'] -= int(line.split(' ')[-1])
        part_2['aim'] -= int(line.split(' ')[-1])
    elif 'for' in line:
        part_1['horizontal position'] += int(line.split(' ')[-1])
        part_2['horizontal position'] += int(line.split(' ')[-1])
        part_2['depth'] += part_2['aim'] * int(line.split(' ')[-1])
    elif 'down' in line:
        part_1['depth'] += int(line.split(' ')[-1])
        part_2['aim'] += int(line.split(' ')[-1])

print(f'The answer to part 1: Depth ({part_1["depth"]}) x Position ({part_1["horizontal position"]})'
      f' = {part_1["depth"] * part_1["horizontal position"]}')
print(f'The answer to part 2: Depth ({part_2["depth"]}) x Position ({part_2["horizontal position"]})'
      f' = {part_2["depth"] * part_2["horizontal position"]}')
