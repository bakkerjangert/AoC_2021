with open('input.txt') as f:
    lines = f.read().splitlines()

crabs = list(map(int, lines[0].split(',')))
start_point, end_point = min(crabs), max(crabs)

fuel_start_point = 0
for crab in crabs:
    fuel_start_point += crab - start_point

crabs_left = crabs.count(start_point)
crabs_right = len(crabs) - crabs_left
position = start_point

fuel = fuel_start_point
for pos in range(start_point + 1, end_point):
    if crabs_left >= crabs_right:
        # minimum found
        position = pos - 1
        break
    else:
        # move up one point
        fuel += crabs_left - crabs_right
        delta_crabs = crabs.count(pos)
        crabs_left += delta_crabs
        crabs_right -= delta_crabs

print(f'Part 1: A minimum of {fuel} fuel is required to reach position {position}')

fuel_consumption = 0
fuel_per_delta = {0: 0}
for delta in range(1, end_point + 1):
    fuel_consumption += delta
    fuel_per_delta[delta] = fuel_consumption

fuel_per_position = dict()
for pos in range(start_point, end_point + 1):
    current_fuel = 0
    for crab in crabs:
        current_fuel += fuel_per_delta[abs(pos - crab)]
    fuel_per_position[pos] = current_fuel

print(f'Part 2: A minimum of {min(fuel_per_position.values())} fuel is required')
