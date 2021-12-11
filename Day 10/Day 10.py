with open('input.txt') as f:
    lines = f.read().splitlines()

scores = {')': 3, ']': 57, '}': 1197, '>': 25137}

good_sub_strings = ('()', '<>', '{}', '[]')
bad_sub_strings = []

for i in range(4):
    for j in range(4):
        string = good_sub_strings[i][0] + good_sub_strings[j][1]
        if string not in good_sub_strings:
            bad_sub_strings.append(string)

answer_part_1 = 0
incomplete_lines = []
counter = -1
for line in lines:
    counter += 1
    while any(a in line for a in good_sub_strings):
        for sub_string in good_sub_strings:
            if sub_string in line:
                index = line.index(sub_string)
                line = line[0:index] + line[index + 2:]
    if not any(a in line for a in bad_sub_strings):
        incomplete_lines.append((line, lines[counter]))
        continue
    indexes = dict()
    for sub_string in bad_sub_strings:
        if sub_string in line:
            index = line.index(sub_string) + 1
            indexes[index] = line[index]
    if len(indexes) > 0:
        char = indexes[min(indexes.keys())]
        answer_part_1 += scores[char]

print(f'The answer to part 1 = {answer_part_1}')

scores = {')': 1, ']': 2, '}': 3, '>': 4}
counterparts = {'(': ')', '[': ']', '{': '}', '<': '>'}
scores_part_2 = []

for line in incomplete_lines:
    score = 0
    for char in line[0][::-1]:
        score = score * 5 + scores[counterparts[char]]
    scores_part_2.append(score)

scores_part_2.sort()

print(f'The answer to Part 2 = {scores_part_2[len(scores_part_2) // 2]}')
