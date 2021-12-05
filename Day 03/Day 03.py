with open('input.txt') as f:
    lines = f.read().splitlines()

def add_lists(list1, list2):
    sum_list = []
    for (item1, item2) in zip(list1, list2):
        sum_list.append(item1+item2)
    return sum_list

data = list(lines[0])

for line in lines[1:]:
    data = add_lists(data, line)

gamma_rate = ''
for item in data:
    if item.count('0') > item.count('1'):
        gamma_rate += '0'
    else:
        gamma_rate += '1'

epsilon_rate = gamma_rate.replace('0', 'x')
epsilon_rate = epsilon_rate.replace('1', '0')
epsilon_rate = epsilon_rate.replace('x', '1')

print(f'The answer to part 1 = gamma ({int(gamma_rate,2)}) x epsilon ({int(epsilon_rate,2)})'
      f' = {int(gamma_rate,2) * int(epsilon_rate,2)}')

def finder(lst, i, mode):
    zeros, ones = [], []
    for item in lst:
        if item[i] == '0':
            zeros.append(item)
        else:
            ones.append(item)
    if mode == 'OX':
        if len(zeros) > len(ones):
            return zeros
        else:
            return ones
    if mode == 'CO2':
        if len(ones) < len(zeros):
            return ones
        else:
            return zeros
    else:
        print('Error!')
        exit()


oxygen = lines.copy()
i = 0
while len(oxygen) > 1:
    oxygen = finder(oxygen, i, 'OX')
    if i == len(oxygen[0]) - 1:
        i = 0
    else:
        i += 1

CO2 = lines.copy()
i = 0
while len(CO2) > 1:
    CO2 = finder(CO2, i, 'CO2')
    if i == len(CO2[0]) - 1:
        i = 0
    else:
        i += 1

print(f'The answer to part 2 = oxygen ({int(oxygen[0],2)}) x CO2 ({int(CO2[0],2)})'
      f' = {int(oxygen[0],2) * int(CO2[0],2)}')
