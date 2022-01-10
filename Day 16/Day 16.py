with open('input.txt') as f:
    lines = f.read().splitlines()

def hex_to_bin(string):
    str_ = ''
    for char in string:
        str_ += convert[char]
    return str_


def version(string):
    return int(string[:3], 2)


def identification(string):
    return int(string[3:6], 2)


def length_type(string):
    return string[6]


class Sub_String():
    def __init__(self, level, string, string_type, ID, length=None, sub_no=None):
        self.level = level
        self.string = string
        self.string_type = string_type
        self.ID = ID
        self.values = []
        self.required_length = length
        self.required_subs = sub_no
        self.finished = False

    def check_if_finished(self):
        if len(self.string) == self.required_length:
            self.finished = True
        if self.required_subs == 0:
            self.finished = True
        if self.string_type == 'literal':
            self.finished = True


def lit_sub_pack(string):
    package = string[:6]
    string = string[6:]
    while True:
        package += string[:5]
        string = string[5:]
        if package[-5] == '0':
            break
    return package, string


def literal_conversion(string):
    number = ''
    string = string[6:]
    while True:
        sub_string = string[:5]
        string = string[5:]
        number += sub_string[1:]
        if sub_string[0] == '0':
            break
    # print(f'Literal number = {int(number, 2)}')
    return int(number, 2)


convert = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
           '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

string_types = {0: 'sub_pack length', 1: 'sub_packnumber', 2: 'literal'}

# string = 'D2FE28'
# string = '38006F45291200'
# string = 'EE00D40C823060'
# string = '8A004A801A8002F478'
# string = '620080001611562C8802118E34'
# string = 'C0015000016115A2E0802F182340'
# string = 'A0016C880162017C3686B18A3D4780'
string = lines[0]

string = hex_to_bin(string)
levels = dict()
finished_levels = dict()
level = 0
sum_versions = 0

while True:
    if len(string) == 0 or '1' not in string:
        break
    VER, ID, LEN = version(string), identification(string), length_type(string)
    # print(f'---CURRENT LEVEL = {level}')
    # print(f'VER = {VER}, ID = {ID}, LEN = {LEN}, Level = {level}, Length = {len(string)} --> {string}')
    sum_versions += VER
    if ID == 4:
        literal, string = lit_sub_pack(string)
        levels[level] = Sub_String(level, literal, string_types[2], ID)
        levels[level].check_if_finished()
        while levels[level].finished:
            levels[level - 1].string += levels[level].string
            if levels[level - 1].string_type == string_types[1]:
                levels[level - 1].required_subs -= 1
            # Add value (Part 2)
            if ID == 0:
                levels[level - 1].values.append(sum(levels[level].values))
            elif ID == 1:
                prod = 1
                for value in levels[level].values:
                    prod *= value
                levels[level - 1].values.append(prod)
            elif ID == 2:
                levels[level - 1].values.append(min(levels[level].values))
            elif ID == 3:
                levels[level - 1].values.append(max(levels[level].values))
            elif ID == 4:
                levels[level - 1].values.append(literal_conversion(levels[level].string))
            elif ID == 5:
                if levels[level].values[0] > levels[level].values[1]:
                    levels[level - 1].values.append(1)
                else:
                    levels[level - 1].values.append(0)
            elif ID == 6:
                if levels[level].values[0] < levels[level].values[1]:
                    levels[level - 1].values.append(1)
                else:
                    levels[level - 1].values.append(0)
            elif ID == 7:
                if levels[level].values[0] == levels[level].values[1]:
                    levels[level - 1].values.append(1)
                else:
                    levels[level - 1].values.append(0)
            # Ending Part 2
            if level not in finished_levels:
                finished_levels[level] = []
            finished_levels[level].append(levels[level])
            del levels[level]
            level -= 1
            ID = levels[level].ID
            levels[level].check_if_finished()
            if level == 0 and levels[level].finished:
                break
    elif LEN == '0':
        length_sub_string = int(string[7:22], 2) + 22
        levels[level] = Sub_String(level, string[:22], string_types[0], ID, length=length_sub_string)
        string = string[22:]
    elif LEN == '1':
        amount_of_subs = int(string[7:18], 2)
        levels[level] = Sub_String(level, string[:18], string_types[1], ID, sub_no=amount_of_subs)
        string = string[18:]
    if level == 0 and levels[level].finished:
        break
    level += 1

print(f'Part 1 = Total version sum = {sum_versions}')
print(f'Part 2 = Total value = {sum(levels[0].values)}')
