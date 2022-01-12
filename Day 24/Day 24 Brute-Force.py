with open('input.txt') as f:
    lines = f.read().splitlines()

def inp(a, val):
    data[a] = val

def add(a, b):
    data[a] += b

def mul(a, b):
    data[a] *= b

def div(a, b):
    data[a] = data[a] // b

def mod(a, b):
    data[a] = data[a] % b

def eql(a, b):
    if data[a] == b:
        data[a] = 1
    else:
        data[a] = 0

def decrease_number(num):
    num = int(num) - 1
    while '0' in str(num):
        num -= 1
    return str(num)


funtions = {'inp': inp, 'add': add, 'mul': mul, 'div': div, 'mod': mod, 'eql': eql}
letters = 'wxyz'
number = '9' * 14
crash = True
while True:
    values = list(map(int, number))
    data = {'w': 0, 'x': 0, 'y': 0, 'z': 0}
    crash = False
    for line in lines:
        prog, a = line.split(' ')[0], line.split(' ')[1]
        if 'inp' in line:
            val = values.pop(0)
            inp(a, val)
            continue
        _ = line.split(' ')[-1]
        if _ in letters:
            b = data[_]
        else:
            b = int(_)
        check_1 = 'div' in line and b == 0
        check_2 = 'mod' in line and data[a] < 0
        check_3 = 'mod' in line and b <= 0
        if check_1 or check_2 or check_3:
            # crash found
            number = decrease_number(number)
            crash = True
            print(f'crashed on number {number}')
            break
        funtions[prog](a, b)
    if not crash:
        print(f'Program terminated correctly at {number}; z-value = {data["z"]}')
        print(values)
        if data['z'] == 0:
            break
        else:
            number = decrease_number(number)
