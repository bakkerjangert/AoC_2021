with open('input.txt') as f:
    lines = f.read().splitlines()

def addition(str1, str2):
    return '[' + str1 + ',' + str2 + ']'

def check_string(string):
    explode_index, split_index = None, None
    nested_level = 0
    current_index = 0
    for i in string:
        if i in delta_level.keys():
            nested_level += delta_level[i]
        if nested_level == 5:
            explode_index = current_index
            break
        current_index += 1
    for i in range(len(string) - 1):
        if string[i: i+2].isnumeric():
            split_index = i
            break
    if explode_index is split_index is None:
        return string, True
    elif explode_index is not None:
        return explode(string, explode_index), False
    else:
        return split(string, split_index), False


def find_number_index(string):
    index = None
    for i in range(len(string)):
        if string[i].isnumeric():
            index = i
            return index
    return index


def explode(string, index):
    # print(f'Exploding "{string}" at index {index}')
    start_index, end_index = index, string.find(']', index)
    numbers = tuple(map(int, string[index + 1:end_index].split(',')))
    # Replace right number (replace from right to left to keep indexes from start pure)
    right_num_start_index = find_number_index(string[end_index:])
    if right_num_start_index is not None:
        right_num_start_index = end_index + right_num_start_index
        right_num_end_index = right_num_start_index
        while True:
            if string[right_num_end_index + 1].isnumeric():
                right_num_end_index += 1
            else:
                break
        new_num_right = int(string[right_num_start_index: right_num_end_index + 1]) + numbers[1]
        string = string[:right_num_start_index] + str(new_num_right) + string[right_num_end_index + 1:]
    # Replace pair
    string = string[:start_index] + '0' + string[end_index + 1:]
    # Replace left number
    left_num_end_index = find_number_index(string[:index][::-1])
    if left_num_end_index is not None:
        left_num_end_index = index - 1 - left_num_end_index
        left_num_start_index = left_num_end_index
        while True:
            if string[left_num_start_index - 1].isnumeric():
                left_num_start_index -= 1
            else:
                break
        new_num_left = int(string[left_num_start_index: left_num_end_index + 1]) + numbers[0]
        string = string[:left_num_start_index] + str(new_num_left) + string[left_num_end_index + 1:]
    return string


def split(string, index):
    # print(f'Splitting "{string}" at index {index}')
    start_index = index
    number = string[index]
    while True:
        if string[index + 1].isnumeric():
            index += 1
            number += string[index]
        else:
            break
    left_num = int(number) // 2
    right_num = int(number) - left_num
    string = string[:start_index] + '[' + str(left_num) + ',' + str(right_num) + ']' + string[index + 1:]
    return string


def magnitude(string):
    while string.count('[') > 1:
        for i in range(len(string)):
            if string[i] == '[':
                if string.find(']', i + 1) < string.find('[', i + 1) or string.find('[', i + 1) == -1:
                    # Inner [] found
                    start_index, end_index = i, string.find(']', i + 1)
                    numbers = tuple(map(int, string[start_index + 1:end_index].split(',')))
                    string = string[:start_index] + str(numbers[0] * 3 + numbers[1] * 2) + string[end_index + 1:]
                    break
        # print(string)
        # input('Pause ...')
    numbers = tuple(map(int, string[1:-1].split(',')))
    return numbers[0] * 3 + numbers[1] * 2


delta_level = {'[': 1, ']': -1}
string = lines[0]
for str2 in lines[1:]:
    string = addition(string, str2)
    reduced = False
    while not reduced:
        val = check_string(string)
        string, reduced = val[0], val[1]
    # print(f'Reduced string --> {string}')
print(f'The answer to part 1 = {magnitude(string)}')

answer_part_2 = 0
number_of_lines = len(lines)

for i in range(number_of_lines):
    for j in range(number_of_lines):
        if i == j:
            continue
        string = addition(lines[i], lines[j])
        reduced = False
        while not reduced:
            val = check_string(string)
            string, reduced = val[0], val[1]
        magnitude_of_string = magnitude(string)
        if magnitude_of_string > answer_part_2:
            answer_part_2 = magnitude_of_string
print(f'The answer to part 2 = {answer_part_2}')
