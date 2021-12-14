with open('input.txt') as f:
    lines = f.read().splitlines()

string = lines[0]
mapping = dict()

for line in lines:
    if '->' in line:
        mapping[line.split(' ')[0]] = line.split(' ')[-1]

# Part 1 --> Brute Force
steps = 10
for step in range(steps):
    new_string = string[0]
    for i in range(1, len(string)):
        new_string += mapping[string[i-1:i+1]] + string[i]
    string = new_string
    # print(f'Part 1 - Step {step + 1} --> len(string) = {len(string)}')

counts = []
for letter in set(string):
    counts.append(string.count(letter))

print(f'The answer to part 1 = {max(counts)} - {min(counts)} = {max(counts) - min(counts)}')

# Part 2 --> with dict with counter
string = lines[0]

counts = dict()
for char in string:
    if char in counts.keys():
        counts[char] += 1
    else:
        counts[char] = 1

data = dict()
for i in range(1, len(string)):
    sub_string = string[i-1:i+1]
    if sub_string in data.keys():
        data[sub_string] += 1
    else:
        data[sub_string] = 1

steps = 40

for step in range(steps):
    sub_strings = tuple()
    new_data = dict()
    for sub_string in data.keys():
        char = mapping[sub_string]
        val = data[sub_string]
        if char in counts.keys():
            counts[char] += val
        else:
            counts[char] = val
        sub_left, sub_right = sub_string[0] + char, char + sub_string[1]
        if sub_left in new_data.keys():
            new_data[sub_left] += val
        else:
            new_data[sub_left] = val
        if sub_right in new_data.keys():
            new_data[sub_right] += val
        else:
            new_data[sub_right] = val
    data = new_data.copy()
    # print(f'Part 2 - Step {step + 1} --> len(string) = {sum(counts.values())}')
    if step == 9:   # Check part 1
        print(f'Checking part 1 --> Step 10 at part 2 = {max(counts.values()) - min(counts.values())}')

print(f'The answer to part 2 = {max(counts.values())} - {min(counts.values())} = {max(counts.values()) - min(counts.values())}')
