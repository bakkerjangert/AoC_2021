with open('input.txt') as f:
    lines = f.read().splitlines()

numbers = {0: ('a', 'b', 'c', 'e', 'f', 'g'),
           1: ('c', 'f'),
           2: ('a', 'c', 'd', 'e', 'g'),
           3: ('a', 'c', 'd', 'f', 'g'),
           4: ('b', 'c', 'd', 'f'),
           5: ('a', 'b', 'd', 'f', 'g'),
           6: ('a', 'b', 'd', 'e', 'f', 'g'),
           7: ('a', 'c', 'f'),
           8: ('a', 'b', 'c', 'd', 'e', 'f', 'g'),
           9: ('a', 'b', 'c', 'd', 'f', 'g')}

mapping_letters = {'a': None, 'b': None, 'c': None, 'd': None, 'e': None, 'f': None, 'g': None}
mapping_numbers = {0: 'x', 1: 'x', 2: 'x', 3: 'x', 4: 'x', 5: 'x', 6: 'x', 7: 'x', 8: 'x', 9: 'x'}

unique_lengths = (len(numbers[1]), len(numbers[4]), len(numbers[7]), len(numbers[8]))
answer_part_1 = 0

for line in lines:
    outputs = line.split(' | ')[-1].split(' ')
    for output in outputs:
        if len(output) in unique_lengths:
            answer_part_1 += 1

print(f'The answer to part 1 = {answer_part_1}')


def determine_a(one, seven):
    for letter in one:
        seven.remove(letter)
    return seven[0]


def determine_b(three, four):
    for letter in three:
        if letter in four:
            four.remove(letter)
    return four[0]


def determine_c(one, six):
    for letter in six:
        if letter in one:
            one.remove(letter)
    return one[0]


def determine_d(one, three, four):
    for letter in one:
        four.remove(letter)
    for letter in three:
        if letter in four:
            return letter


def determine_e(eight, nine):
    for letter in nine:
        eight.remove(letter)
    return eight[0]


def determine_f(one, two):
    for letter in two:
        if letter in one:
            one.remove(letter)
    return one[0]


def determine_g(eight):
    for letter in ('a', 'b', 'c', 'd', 'e', 'f'):
        eight.remove(cur_let[letter])
    return eight[0]


output_numbers = list()

for line in lines:
    outputs = line.split(' | ')[-1].split(' ')
    data = line.split(' | ')[0].split(' ')
    cur_num = mapping_numbers.copy()
    cur_let = mapping_letters.copy()
    # First map 1,3,4, 7 and 8
    for item in data:
        if len(item) == 2:
            cur_num[1] = item
        if len(item) == 3:
            cur_num[7] = item
        if len(item) == 4:
            cur_num[4] = item
        if len(item) == 7:
            cur_num[8] = item
    for item in data:
        if len(item) == 5 and all(a in item for a in cur_num[1]):
            cur_num[3] = item
    for item in data:
        if len(item) == 6 and all(a in item for a in cur_num[3]):
            cur_num[9] = item

    cur_let['a'] = determine_a(list(cur_num[1]), list(cur_num[7]))
    cur_let['b'] = determine_b(list(cur_num[3]), list(cur_num[4]))
    cur_let['d'] = determine_d(list(cur_num[1]), list(cur_num[3]), list(cur_num[4]))

    for item in data:
        if len(item) == 6 and (cur_let['d'] not in item):
            cur_num[0] = item
        if len(item) == 5 and (cur_let['a'] in item and cur_let['b'] in item and cur_let['d'] in item):
            cur_num[5] = item
    for item in data:
        if len(item) == 5 and sorted(cur_num[3]) != sorted(item) and sorted(cur_num[5]) != sorted(item):
            cur_num[2] = item
        if len(item) == 6 and (not all(a in item for a in cur_num[1])):
            cur_num[6] = item

    cur_let['c'] = determine_c(list(cur_num[1]), list(cur_num[6]))
    cur_let['e'] = determine_e(list(cur_num[8]), list(cur_num[9]))
    cur_let['f'] = determine_f(list(cur_num[1]), list(cur_num[2]))
    cur_let['g'] = determine_g(list(cur_num[8]))

    cur_num_reversed = dict()
    for i in range(10):
        cur_num_reversed[tuple(sorted(cur_num[i]))] = str(i)

    number = ''
    for item in outputs:
        number += cur_num_reversed[tuple(sorted(list(item)))]
    output_numbers.append(int(number))
    # print(data)
    # print(f'-- Number = {number}')
    # for i in ('a', 'b', 'c', 'd', 'e', 'f', 'g'):
    #     print(f'Letter {i} --> {cur_let[i]}')
    # for i in range(10):
    #     print(f'Number {i} --> {cur_num[i]}')
    # for i in cur_num_reversed.keys():
    #     print(f'{i} --> Number {cur_num_reversed[i]}')

print(f'The answer to part 2 = {sum(output_numbers)}')
