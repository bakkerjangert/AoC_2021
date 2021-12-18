# with open('input.txt') as f:
#     lines = f.read().splitlines()

def analyse_hexa(data):
    if data[1] == 'HEX':
        str_ = ''
        for char in data[0]:
            str_ += convert[char]
        print(str_)
    elif data[1] == 'BIN':
        str_ = data[0]
    VER = int(str_[:3], 2)
    ID = int(str_[3:6], 2)
    print(f'{string} --> Version = {VER}; ID = {ID}')
    if ID == 4:
        lit_num = literal(str_[6:])
    len_ID = str_[6]
    if ID != 4 and len_ID == '0':
        print(f'Len ID = {len_ID}')
        len_sub = int(str_[7: 7 + 15], 2)
        print(f'len_sub = {len_sub}')
        string_left = str_[22:]
        while len_sub > 0:
            sub_string, string_left = gen_sub_string(string_left)
            len_sub -= len(sub_string)
            print(f'Len sub = {len_sub}')
            val = (sub_string, 'BIN')
            strings.append(val)
    if ID != 4 and len_ID == '1':
        print(f'Len ID = {len_ID}')
        amount_of_subs = int(str_[7: 7 + 11], 2)
        print(f'sub packs = {amount_of_subs}')
        string_left = str_[18:]
        for i in range(amount_of_subs):
            sub_string, string_left = gen_sub_string(string_left)
            val = (sub_string, 'BIN')
            strings.append(val)
    return VER

def gen_sub_string(string):
    str_ = string[:6]
    string = string[6:]
    while True:
        str_ += string[:5]
        string = string[5:]
        if str_[-5] == '0':
            break
    return str_, string


def literal(string):
    number = ''
    while True:
        sub_string = string[:5]
        string = string[5:]
        number += sub_string[1:]
        if sub_string[0] == '0':
            break
    print(f'Literal number = {int(number, 2)}')
    return number


convert = {'0': '0000',
           '1': '0001',
           '2': '0010',
           '3': '0011',
           '4': '0100',
           '5': '0101',
           '6': '0110',
           '7': '0111',
           '8': '1000',
           '9': '1001',
           'A': '1010',
           'B': '1011',
           'C': '1100',
           'D': '1101',
           'E': '1110',
           'F': '1111',}


# strings = [('D2FE28', 'HEX')]
# strings = [('38006F45291200', 'HEX')]
# strings = [('EE00D40C823060', 'HEX')]
# strings = [('8A004A801A8002F478', 'HEX')]
strings = [('620080001611562C8802118E34', 'HEX')]
# strings = ['C0015000016115A2E0802F182340']
# strings = ['A0016C880162017C3686B18A3D4780']
version_sum = 0
while len(strings) > 0:
    string = strings.pop(0)
    print(f'--- Analyse string "{string}" ---')
    version_sum += analyse_hexa(string)
    print(strings)
print(f'Total version sum = {version_sum}')

for string in strings:
    version = analyse_hexa(string)
