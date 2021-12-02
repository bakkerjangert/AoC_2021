with open('input.txt') as f:
    lines = f.read().splitlines()

depths = list(map(int, lines))
depth_increase_counter_part_1 = 0
depth_increase_counter_part_2 = 0

for i in range(len(depths)):
    # Part 1
    if i < len(depths) - 1:
        if depths[i + 1] > depths[i]:
            depth_increase_counter_part_1 += 1
    else:
        pass
    # Part 2
    if i < len(depths) - 3:
        if depths[i + 1] + depths[i + 2] + depths[i + 3] > depths[i] + depths[i + 1] + depths[i + 2]:
        # if sum(depths[i + 1: i + 4]) > sum(depths[i: i + 3]):  # Carefull --> No index error on end!
            depth_increase_counter_part_2 += 1
    else:
        pass

print(f'The answer to part 1: The depths increases {depth_increase_counter_part_1} times')
print(f'The answer to part 2: The depths increases {depth_increase_counter_part_2} times')


test = [0, 1, 2]
print(sum(test[0:8]))  # Why does this not result in an index error????

test_2 = test[7:8]
print(test_2)