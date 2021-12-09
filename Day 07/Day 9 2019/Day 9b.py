with open('input.txt') as f:
    lines = f.read().splitlines()

prog_lst = list(map(int, lines[0].split(',')))

prog = {}

for i in range(len(prog_lst)):
    prog[i] = prog_lst[i]

####################################################################
## NOTE --> Might need to add system to read from unknown memory! ##
####################################################################

def op_1(prog, pos, rel_val):
    index_1 = prog[pos + 1]
    index_2 = prog[pos + 2]
    index_3 = prog[pos + 3]
    code = str(prog[pos])
    while len(code) < 5:
        code = '0' + code
    # print(code)
    # Set val_1
    if code[2] == '1':
        val_1 = prog[pos + 1]
    elif code[2] == '2':
        val_1 = prog[rel_val + index_1]
    elif code[2] == '0':
        val_1 = prog[index_1]
    else:
        print('Error! Unknown method code!')
        exit()
    # Set val_2
    if code[1] == '1':
        val_2 = prog[pos + 2]
    elif code[1] == '2':
        val_2 = prog[rel_val + index_2]
    elif code[1] == '0':
        val_2 = prog[index_2]
    else:
        print('Error! Unknown method code!')
        exit()
    # write value
    if code[0] == '1':
        prog[pos + 3] = val_1 + val_2
    elif code[0] == '2':
        prog[rel_val + index_3] = val_1 + val_2
    elif code[0] == '0':
        prog[index_3] = val_1 + val_2
    else:
        print('Error! Unknown method code!')
        exit()
    pos += 4
    return pos


def op_2(prog, pos, rel_val):
    index_1 = prog[pos + 1]
    index_2 = prog[pos + 2]
    index_3 = prog[pos + 3]
    code = str(prog[pos])
    while len(code) < 5:
        code = '0' + code
    # print(code)
    # Set val_1
    if code[2] == '1':
        val_1 = prog[pos + 1]
    elif code[2] == '2':
        val_1 = prog[index_1 + rel_val]
    elif code[2] == '0':
        val_1 = prog[index_1]
    else:
        print('Error! Unknown method code!')
        exit()
    # Set val_2
    if code[1] == '1':
        val_2 = prog[pos + 2]
    elif code[1] == '2':
        val_2 = prog[rel_val + index_2]
    elif code[1] == '0':
        val_2 = prog[index_2]
    else:
        print('Error! Unknown method code!')
        exit()
    # Write value
    if code[0] == '1':
        prog[pos + 3] = val_1 * val_2
    elif code[0] == '2':
        prog[rel_val + index_3] = val_1 * val_2
    elif code[0] == '0':
        prog[index_3] = val_1 * val_2
    else:
        print('Error! Unknown method code!')
        exit()
    pos += 4
    return pos


def op_3(prog, pos, input_val, rel_val):
    index_1 = prog[pos + 1]
    code = str(prog[pos])
    while len(code) < 3:
        code = '0' + code
    if code[0] == '1':
        prog[pos + 1] = input_val
    elif code[0] == '2':
        prog[rel_val + index_1] = input_val
    elif code[0] == '0':
        prog[index_1] = input_val
    else:
        print('Error! Unknown method code!')
        exit()
    pos += 2
    return pos


def op_4(prog, pos, rel_val):
    index_1 = prog[pos + 1]
    code = str(prog[pos])
    while len(code) < 3:
        code = '0' + code
    if code[0] == '1':
        output = prog[pos + 1]
    elif code[0] == '2':
        output = prog[rel_val + index_1]
    elif code[0] == '0':
        output = prog[index_1]
    else:
        print('Error! Unknown method code!')
        exit()
    pos += 2
    print(f'Output = {output}')
    return pos, output


def op_5(prog, pos, rel_val):
    change = False
    index_1 = prog[pos + 1]
    index_2 = prog[pos + 2]
    code = str(prog[pos])
    while len(code) < 5:
        code = '0' + code
    # print(code)
    # Set val_1
    if code[2] == '1':
        val_1 = prog[pos + 1]
    elif code[2] == '2':
        val_1 = prog[rel_val + index_1]
    elif code[2] == '0':
        val_1 = prog[index_1]
    else:
        print('Error! Unknown method code!')
        exit()
    # Set val_2
    if code[1] == '1':
        val_2 = prog[pos + 2]
    elif code[1] == '2':
        val_2 = prog[rel_val + index_2]
    elif code[1] == '0':
        val_2 = prog[index_2]
    else:
        print('Error! Unknown method code!')
        exit()
    if val_1 != 0:  # Check wether this still works for Day 9
        pos = val_2
        change = True
    if not change:
        pos += 3  # Check --> This op only regards 2 values; should be +3 instead of +4?
    return pos


def op_6(prog, pos, rel_val):
    change = False
    index_1 = prog[pos + 1]
    index_2 = prog[pos + 2]
    code = str(prog[pos])
    while len(code) < 5:
        code = '0' + code
    # print(code)
    # Set val_1
    if code[2] == '1':
        val_1 = prog[pos + 1]
    elif code[2] == '2':
        val_1 = prog[rel_val + index_1]
    elif code[2] == '0':
        val_1 = prog[index_1]
    else:
        print('Error! Unknown method code!')
        exit()
    # Set val_2
    if code[1] == '1':
        val_2 = prog[pos + 2]
    elif code[1] == '2':
        val_2 = prog[rel_val + index_2]
    elif code[1] == '0':
        val_2 = prog[index_2]
    else:
        print('Error! Unknown methode code!')
        exit()
    if val_1 == 0:  # Check wether this still works for Day 9
        pos = val_2
        change = True
    if not change:
        pos += 3  # Check --> This op only regards 2 values; should be +3 instead of +4?
    return pos


def op_7(prog, pos, rel_val):
    index_1 = prog[pos + 1]
    index_2 = prog[pos + 2]
    index_3 = prog[pos + 3]
    code = str(prog[pos])
    while len(code) < 5:
        code = '0' + code
    # print(code)
    # Set val_1
    if code[2] == '1':
        val_1 = prog[pos + 1]
    elif code[2] == '2':
        val_1 = prog[rel_val + index_1]
    elif code[2] == '0':
        val_1 = prog[index_1]
    else:
        print('Error! Unknown method code!')
        exit()
    # Set val_2
    if code[1] == '1':
        val_2 = prog[pos + 2]
    elif code[1] == '2':
        val_2 = prog[rel_val + index_2]
    elif code[1] == '0':
        val_2 = prog[index_2]
    else:
        print('Error! Unknown method code!')
        exit()
    if val_1 < val_2:
        if code[0] == '1':
            prog[pos + 3] = 1
        elif code[0] == '2':
            prog[rel_val + index_3] = 1
        elif code[0] == '0':
            prog[index_3] = 1
        else:
            print('Error! Unknown method code!')
            exit()
    else:
        if code[0] == '1':
            prog[pos + 3] = 0
        elif code[0] == '2':
            prog[rel_val + index_3] = 0
        elif code[0] == '0':
            prog[index_3] = 0
        else:
            print('Error! Unknown method code!')
            exit()
    pos += 4
    return pos


def op_8(prog, pos, rel_val):
    index_1 = prog[pos + 1]
    index_2 = prog[pos + 2]
    index_3 = prog[pos + 3]
    code = str(prog[pos])
    while len(code) < 5:
        code = '0' + code
    # print(code)
    # Set val_1
    if code[2] == '1':
        val_1 = prog[pos + 1]
    elif code[2] == '2':
        val_1 = prog[rel_val + index_1]
    elif code[2] == '0':
        val_1 = prog[index_1]
    else:
        print('Error! Unknown method code!')
        exit()
    # Set val_2
    if code[1] == '1':
        val_2 = prog[pos + 2]
    elif code[1] == '2':
        val_2 = prog[rel_val + index_2]
    elif code[1] == '0':
        val_2 = prog[index_2]
    else:
        print('Error! Unknown method code!')
        exit()
    if val_1 == val_2:
        if code[0] == '1':
            prog[pos + 3] = 1
        elif code[0] == '2':
            prog[rel_val + index_3] = 1
        elif code[0] == '0':
            prog[index_3] = 1
        else:
            print('Error! Unknown method code!')
            exit()
    else:
        if code[0] == '1':
            prog[pos + 3] = 0
        elif code[0] == '2':
            prog[rel_val + index_3] = 0
        elif code[0] == '0':
            prog[index_3] = 0
        else:
            print('Error! Unknown method code!')
            exit()
    pos += 4
    return pos


def op_9(prog, pos, rel_val):
    index_1 = prog[pos + 1]
    code = str(prog[pos])
    while len(code) < 3:
        code = '0' + code
    if code[0] == '1':
        rel_val += prog[pos + 1]
    elif code[0] == '2':
        rel_val += prog[rel_val + index_1]
    elif code[0] == '0':
        rel_val += prog[index_1]
    else:
        print('Error! Unknown method code!')
        exit()
    pos += 2
    return pos, rel_val

input_val = 2
rel_val = 0

output = None
pos = 0

#TEST
# prog = {0: 109, 1: 1, 2: 204, 3: -1, 4: 1001, 5: 100, 6: 1, 7: 100, 8: 1008, 9: 100, 10: 16, 11: 101, 12: 1006, 13: 101, 14: 0, 15: 99}
# prog = {0: 1102, 1: 34915192, 2: 34915192, 3: 7, 4: 4, 5: 7, 6: 99, 7: 0}
# prog = [1102,34915192,34915192,7,4,7,99,0]
# prog = {0: 104, 1: 1125899906842624, 2: 99}


while True:
    icode = prog[pos] % 100
    if icode == 1:
        pos = op_1(prog, pos, rel_val)
    elif icode == 2:
        pos = op_2(prog, pos, rel_val)
    elif icode == 3:
        pos = op_3(prog, pos, input_val, rel_val)
    elif icode == 4:
        tup = op_4(prog, pos, rel_val)
        pos = tup[0]
        output = tup[1]
    elif icode == 5:
        pos = op_5(prog, pos, rel_val)
    elif icode == 6:
        pos = op_6(prog, pos, rel_val)
    elif icode == 7:
        pos = op_7(prog, pos, rel_val)
    elif icode == 8:
        pos = op_8(prog, pos, rel_val)
    elif icode == 9:
        tup = op_9(prog, pos, rel_val)
        pos = tup[0]
        rel_val = tup[1]

    elif icode == 99:
        print(f'The answer = {output}')
        exit()
    else:
        print('Danger! Danger! Unknown input command!!!')
        break
