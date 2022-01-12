with open('input.txt') as f:
    lines = f.read().splitlines()

def decrease_number(num):
    n = int(num) - 1
    while '0' in str(n):
        n -= 1
    if n > 0 and len(num) == len(str(n)):
        return str(n)
    else:
        return None

def print_dict(dct):
    for key in dct:
        print(f'{key} --> {dct[key]}')

w = '9' * 14
factor = int(lines[9].split(' ')[-1]) + 1

xs, ys, zs = [], [], []
delta = 18
for i in range(14):
    xs.append(int(lines[5 + delta * i].split(' ')[-1]))
    ys.append(int(lines[15 + delta * i].split(' ')[-1]))
    zs.append(int(lines[4 + delta * i].split(' ')[-1]))

print(xs)
print(ys)
print(zs)

first_parts = {}
w = '9' * 5
while True:
    z = 0
    for i, num in enumerate(w):
        num = int(num)
        if z % 26 + xs[i] != num:
            z = (z // zs[i]) * factor + ys[i] + num
        else:
            z = z // zs[i]
            if i == 4:
                if z not in first_parts.keys():
                    first_parts[z] = [w]
                else:
                    first_parts[z].append(w)
                # print(f'{w} --> z = {z}')
    w = decrease_number(w)
    if w is None:
        break

print_dict(first_parts)
print(len(first_parts))

second_parts = {}

w = '9' * 3
while True:
    for z in first_parts.keys():
        z_init = z
        for i, num in enumerate(w):
            num = int(num)
            if z % 26 + xs[i + 5] != num:
                z = (z // zs[i + 5]) * factor + ys[i + 5] + num
            else:
                z = z // zs[i + 5]
                if i == 2:
                    if (z_init, z) not in second_parts.keys():
                        second_parts[(z_init, z)] = [w]
                    else:
                        second_parts[(z_init, z)].append(w)
    w = decrease_number(w)
    if w is None:
        break

print_dict(second_parts)
print(len(second_parts))

third_parts = {}
w = '9' * 2
while True:
    for z_init in second_parts.keys():
        z = z_init[-1]
        for i, num in enumerate(w):
            num = int(num)
            if z % 26 + xs[i + 8] != num:
                z = (z // zs[i + 8]) * factor + ys[i + 8] + num
            else:
                z = z // zs[i + 8]
                if i == 1:
                    if z_init + (z,) not in third_parts.keys():
                        third_parts[z_init + (z,)] = [w]
                    else:
                        third_parts[z_init + (z,)].append(w)
                    # print(f'z = {z}')
    w = decrease_number(w)
    if w is None:
        break
print_dict(third_parts)
print(len(third_parts))
# input('pause')


fourth_parts = {}
w = '9' * 1
while True:
    for z_init in third_parts.keys():
        z = z_init[-1]
        for i, num in enumerate(w):
            num = int(num)
            if z % 26 + xs[i + 10] != num:
                z = (z // zs[i + 10]) * factor + ys[i + 10] + num
            else:
                z = z // zs[i + 10]
                if i == 0:
                    if z_init + (z,) not in fourth_parts.keys():
                        fourth_parts[z_init + (z,)] = [w]
                    else:
                        fourth_parts[z_init + (z,)].append(w)
                    # print(f'z = {z}')
    w = decrease_number(w)
    if w is None:
        break
print_dict(fourth_parts)
print(len(fourth_parts))
# input('pause')

fifth_parts = {}
w = '9' * 1
while True:
    for z_init in fourth_parts.keys():
        z = z_init[-1]
        for i, num in enumerate(w):
            num = int(num)
            if z % 26 + xs[i + 11] != num:
                z = (z // zs[i + 11]) * factor + ys[i + 11] + num
            else:
                z = z // zs[i + 11]
                if i == 0:
                    if z_init + (z,) not in fifth_parts.keys():
                        fifth_parts[z_init + (z,)] = [w]
                    else:
                        fifth_parts[z_init + (z,)].append(w)
                    # print(f'z = {z}')
    w = decrease_number(w)
    if w is None:
        break
print_dict(fifth_parts)
print(len(fifth_parts))

sixth_parts = {}
w = '9' * 1
while True:
    for z_init in fifth_parts.keys():
        z = z_init[-1]
        for i, num in enumerate(w):
            num = int(num)
            if z % 26 + xs[i + 12] != num:
                z = (z // zs[i + 12]) * factor + ys[i + 12] + num
            else:
                z = z // zs[i + 12]
                if i == 0:
                    if z_init + (z,) not in sixth_parts.keys():
                        sixth_parts[z_init + (z,)] = [w]
                    else:
                        sixth_parts[z_init + (z,)].append(w)
                    # print(f'z = {z}')
    w = decrease_number(w)
    if w is None:
        break
print_dict(sixth_parts)
print(len(sixth_parts))

seventh_parts = {}
w = '9' * 1
while True:
    for z_init in sixth_parts.keys():
        z = z_init[-1]
        for i, num in enumerate(w):
            num = int(num)
            if z % 26 + xs[i + 13] != num:
                z = (z // zs[i + 13]) * factor + ys[i + 13] + num
            else:
                z = z // zs[i + 13]
                if i == 0:
                    if z_init + (z,) not in seventh_parts.keys():
                        seventh_parts[z_init + (z,)] = [w]
                    else:
                        seventh_parts[z_init + (z,)].append(w)
                    # print(f'z = {z}')
    w = decrease_number(w)
    if w is None:
        break
print_dict(seventh_parts)
print(len(seventh_parts))

print(xs)
print(ys)
print(zs)

zero_answers = []

for key in seventh_parts.keys():
    val7 = seventh_parts[key][0]
    if key[:-1] in sixth_parts.keys():
        for val6 in sixth_parts[key[:-1]]:
            if key[:-2] in fifth_parts.keys():
                for val5 in fifth_parts[key[:-2]]:
                    if key[:-3] in fourth_parts.keys():
                        for val4 in fourth_parts[key[:-3]]:
                            if key[:-4] in third_parts.keys():
                                for val3 in third_parts[key[:-4]]:
                                    if key[:-5] in second_parts.keys():
                                        for val2 in second_parts[key[:-5]]:
                                            if key[0] in first_parts.keys():
                                                for val1 in first_parts[key[0]]:
                                                    zero_answers.append(val1 + val2 + val3 + val4 + val5 + val6 + val7)
                                                    print(val1 + val2 + val3 + val4 + val5 + val6 + val7)


print(f'Part 1: Max val = {max(zero_answers)}')
print(f'Part 2: Min val = {min(zero_answers)}')
