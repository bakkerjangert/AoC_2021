#     0123456789A        with A = 10
#    #############
#    #...........# hall
#    ###C#D#D#A### 0
#      #D#C#B#A#   1
#      #D#B#A#C#   2
#      #B#A#B#C#   3
#      #########
#       a b c d
#
# AoC 2021 - Day 23 - Part 2 including personal puzzle input

class Board():
    def __init__(self):
        self.a = ['C', 'D', 'D', 'B']
        self.b = ['D', 'C', 'B', 'A']
        self.c = ['D', 'B', 'A', 'B']
        self.d = ['A', 'A', 'C', 'C']
        self.moves = []
        self.scores = []
        self.hall = [[], [], [], [], [], [], [], [], [], [], []]
        self.hall_postions = (0, 1, 3, 5, 7, 9, 10)
        self.costs = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
        self.lst_ad = [self.a, self.b, self.c, self.d]
        self.ad_index = {'a': 0, 'b': 1, 'c': 2, 'd': 3}
        self.ad_hall_index = {'a': 2, 'b': 4, 'c': 6, 'd': 8}
        self.ad_return = {'a': False, 'b': False, 'c': False, 'd': False}
        self.ad_finished = {'a': False, 'b': False, 'c': False, 'd': False}

    def move_out(self, ad, hall_index):
        # Manual move out
        self.moves.append((ad, hall_index))
        lst = self.lst_ad[self.ad_index[ad]]
        char = lst.pop(0)
        self.hall[hall_index].append(char)
        # Add score
        steps = 4 - len(lst) + abs(self.ad_hall_index[ad] - hall_index)
        self.scores.append(steps * self.costs[char])
        # Check if returning possible
        if len(lst) == 0 or all(letter in lst for letter in [ad.upper]):
            self.ad_return[ad] = True

    def move_in(self):
        # Automatic move in
        moved = 999
        while moved > 0:
            moved = 0
            # First move from hallway
            for index, lst in enumerate(self.hall):
                if len(lst) == 0:
                    continue
                char = lst[0]
                if not self.ad_return[char.lower()]:
                    continue
                goal_index = self.ad_hall_index[char.lower()]
                if index < goal_index:
                    path = self.hall[index + 1: goal_index + 1]
                else:
                    path = self.hall[goal_index: index]
                if not path.count([]) == len(path):
                    # path is blocked
                    continue
                moved += 1
                self.moves.append((index, char.lower()))
                self.lst_ad[self.ad_index[char.lower()]].append(char)
                self.hall[index].clear()
                if len(self.lst_ad[self.ad_index[char.lower()]]) == 4:
                    self.ad_finished[char.lower()] = True
                # Add score
                steps = abs(index - goal_index) + 5 - len(self.lst_ad[self.ad_index[char.lower()]])
                self.scores.append(steps * self.costs[char])
            # Then move from other lines directly
            for lane in ('a', 'b', 'c', 'd'):
                lst = self.lst_ad[self.ad_index[lane]]
                if len(lst) == 0:
                    continue
                if self.ad_return[lane]:
                    continue
                char = lst[0]
                if lane == char.lower():
                    continue
                index, goal_index = self.ad_hall_index[lane], self.ad_hall_index[char.lower()]
                if not self.ad_return[char.lower()]:
                    continue
                if index < goal_index:
                    path = self.hall[index + 1: goal_index + 1]
                else:
                    path = self.hall[goal_index: index]
                if not path.count([]) == len(path):
                    # path is blocked
                    continue
                moved += 1
                self.moves.append((lane, char.lower()))
                self.lst_ad[self.ad_index[char.lower()]].append(char)
                lst.pop(0)
                if len(self.lst_ad[self.ad_index[char.lower()]]) == 4:
                    self.ad_finished[char.lower()] = True
                if len(lst) == 0 or all(letter in lst for letter in [lane.upper]):
                    self.ad_return[lane] = True
                # add score!
                steps = (4 - len(lst)) + abs(index - goal_index) + 5 - (len(self.lst_ad[self.ad_index[char.lower()]]))
                self.scores.append(steps * self.costs[char])

    def get_previous_state(self):
        while True:
            move = self.moves.pop(-1)
            del self.scores[-1]
            if type(move[0]) == type(move[1]) == type('foobar'):   # Moving back from lane to lane
                char = self.lst_ad[self.ad_index[move[1]]].pop(-1)
                self.lst_ad[self.ad_index[move[0]]].insert(0, char)
                self.ad_finished[move[1]] = False
                self.ad_return[move[0]] = False
            elif type(move[1]) == type('foobar'):   # Moving back from lane to hall
                char = self.lst_ad[self.ad_index[move[1]]].pop(-1)
                self.hall[move[0]].append(char)
                self.ad_finished[move[1]] = False
            else:
                char = self.hall[move[1]].pop(0)   # Moving back from hall to lane
                self.lst_ad[self.ad_index[move[0]]].insert(0, char)
                self.ad_return[move[0]] = False
                break

    def get_valid_moves(self):
        valid_moves = []
        for lane in ('a', 'b', 'c', 'd'):
            if self.ad_finished[lane] or self.ad_return[lane]:
                continue
            start_index = self.ad_hall_index[lane]
            for i in range(start_index, 11):
                if i not in self.hall_postions:
                    continue
                if self.hall[i] == []:
                    valid_moves.append([lane, i])
                else:
                    break
            for i in range(start_index, -1, -1):
                if i not in self.hall_postions:
                    continue
                if self.hall[i] == []:
                    valid_moves.append([lane, i])
                else:
                    break
        return sorted(valid_moves, key=lambda x: x[1])

    def __repr__(self):
        lines = [''] * 7
        lines[0] = '#' * 13 + '\n'
        lines[6] = '  #########  \n'
        sides = '#', '###', '  #', '  #', '  #'
        for i in range(1, 6):
            lines[i] += sides[i - 1]
        for i in range(len(self.hall)):
            if not self.hall[i]:
                lines[1] += '.'
            else:
                lines[1] += self.hall[i][0]
        lst_len = (4, 3, 2, 1)
        for lst in self.lst_ad:
            for i in range(4):
                if len(lst) < lst_len[i]:
                    lines[2 + i] += '.' + '#'
                else:
                    lines[2 + i] += lst[i - (4 - len(lst))] + '#'
        sides = '#\n', '##\n', '  \n', '  \n', '  \n'
        for i in range(1, 6):
            lines[i] += sides[i - 1]
        return ''.join(lines)

board = Board()
valid_paths = dict()
levels = {0: board.get_valid_moves()}
level = 0
iteration = 0
while True:
    iteration += 1
    if iteration % 10000 == 0:
        print(f'--- Status at iteration {iteration} ---')
        print(board)
    if level == 0 and len(levels[0]) == 0:
        break
    elif len(levels[level]) == 0:
        level -= 1
        if False not in board.ad_finished.values():
            valid_paths[tuple(map(tuple, board.moves))] = sum(board.scores)
            print(f'--- Valid path found! ---')
            print(board.moves)
            print(f'Total score of {sum(board.scores)}')
            input('Pause ...')
        board.get_previous_state()
    else:
        next_move = levels[level].pop(0)
        board.move_out(next_move[0], next_move[1])
        board.move_in()
        level += 1
        levels[level] = board.get_valid_moves()

for key, val in valid_paths.items():
    print(key)
    print(val)
    print('')


# Test Case
# board = Board()
# print(board.get_valid_moves())
# board.move_out('a', 5)
# print(board.get_valid_moves())
# board.move_out('a', 10)
# board.move_out('a', 9)
# board.move_out('a', 1)
# board.move_in()
# print(board)
# print(f'\n{board.moves}')
# print(board.scores)
# board.move_out('d', 3)
# board.move_out('d', 5)
# print(board)
# print(f'\n{board.moves}')
# print(board.scores)
# board.move_in()
# print(board)
# print(f'\n{board.moves}')
# print(board.scores)
# board.get_previous_state()
# print(board)
# print(f'\n{board.moves}')
# print(board.scores)
# board.get_previous_state()
# print(board)
# print(f'\n{board.moves}')
# print(board.scores)
# board.get_previous_state()
# print(board)
# print(f'\n{board.moves}')
# print(board.scores)
# board.get_previous_state()
# print(board)
# print(f'\n{board.moves}')
# print(board.scores)
# board.get_previous_state()
# print(board)
# print(f'\n{board.moves}')
# print(board.scores)
#
# board.get_previous_state()
# print(board)
# print(f'\n{board.moves}')
# print(board.scores)