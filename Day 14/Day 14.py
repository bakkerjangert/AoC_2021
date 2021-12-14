with open('input.txt') as f:
    lines = f.read().splitlines()

string = lines[0]
mapping = dict()
clean_data = dict()

for line in lines:
    if '->' in line:
        mapping[line.split(' ')[0]] = line.split(' ')[-1]
        clean_data[line.split(' ')[0]] = 0

letter_count = dict()
for char in list(string) + list(mapping.values()):
    letter_count[char] = 0
for char in string:
    letter_count[char] += 1

data = clean_data.copy()
for i in range(1, len(string)):
    data[string[i-1:i+1]] += 1

steps_1 = 10
steps_2 = 40

for step in range(steps_2):
    new_data = clean_data.copy()
    for sub_string in data.keys():
        char = mapping[sub_string]
        val = data[sub_string]
        letter_count[char] += val
        sub_left, sub_right = sub_string[0] + char, char + sub_string[1]
        new_data[sub_left] += val
        new_data[sub_right] += val
    data = new_data.copy()
    if step == steps_1 - 1:   # Part 1
        print(f'The answer to part 1 = {max(letter_count.values())} - {min(letter_count.values())} = {max(letter_count.values()) - min(letter_count.values())}')
print(f'The answer to part 2 = {max(letter_count.values())} - {min(letter_count.values())} = {max(letter_count.values()) - min(letter_count.values())}')
