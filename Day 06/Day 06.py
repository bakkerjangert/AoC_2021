with open('input.txt') as f:
    lines = f.read().splitlines()

fishes = list(map(int, lines[0].split(',')))

fish_dict = {}
for i in range(9):
    fish_dict[i] = fishes.count(i)

sample_fish = [0]
sample_dict = {}
days = 256 // 2
for day in range(days):
    for i in range(len(sample_fish.copy())):
        if sample_fish[i] == 0:
            sample_fish[i] = 6
            sample_fish.append(8)
        else:
            sample_fish[i] -= 1
    if (70 < day < 80) or 118 < day < 128:
        sample_dict[day + 1] = sample_fish.copy()

answer_part_1 = 0
for i in range(9):
    answer_part_1 += len(sample_dict[80 - i]) * fish_dict[i]

print(f'Part 1: There are {answer_part_1} fishes after 80 days')

sample_dict_128 = {}
for day in range(128 - 8, 128 + 1):
    sample_dict_128[day] = dict()
    for i in range(9):
        sample_dict_128[day][i] = sample_dict[day].count(i)

answer_part_2 = 0
for i in range(9):
    for j in range(9):
        answer_part_2 += fish_dict[i] * sample_dict_128[128 - i][j] * len(sample_dict[128 - j])

print(f'Part 2: There are {answer_part_2} fishes after 256 days (calculated as 2 x 128 days)')
