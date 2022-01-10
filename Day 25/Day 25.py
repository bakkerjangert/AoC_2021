from copy import deepcopy
class Cucumbers():
    def __init__(self, x_max, y_max):
        self.east_positions = []
        self.south_positions = []
        self.X_MAX, self.Y_MAX = x_max, y_max
        self.previous_east_state = None
        self.previous_south_state = None

    def add_east_cucumber(self, cumcumber):
        self.east_positions.append(cumcumber.position)

    def add_south_cucumber(self, cumcumber):
        self.south_positions.append(cumcumber.position)

    def set_previous_state(self):
        self.previous_east_state = deepcopy(self.east_positions)
        self.previous_south_state = deepcopy(self.south_positions)

    def check_final_state(self):
        if self.east_positions == self.previous_east_state and self.south_positions == self.previous_south_state:
            return True
        return False

    def print_state(self):
        for y in range(self.Y_MAX):
            for x in range(self.X_MAX):
                if [x, y] in self.east_positions:
                    char = '>'
                elif [x, y] in self.south_positions:
                    char = 'v'
                else:
                    char = '.'
                print(char, end='')
            print('')


class East_Cucumber():
    def __init__(self, x, y, max_range):
        self.MAX_RANGE = max_range
        self.position = [x, y]
        self.new_position = None
        self.move = False

    def get_new_position(self):
        if self.position[0] == self.MAX_RANGE:
            self.new_position = [0, self.position[1]]
        else:
            self.new_position = [self.position[0] + 1, self.position[1]]

    def check_move(self, cucumbers):
        self.get_new_position()
        if self.new_position not in cucumbers.south_positions and self.new_position not in cucumbers.east_positions:
            self.move = True

    def do_move(self):
        if self.move:
            self.position[0], self.position[1] = self.new_position
        self.move = False


class South_Cucumber():
    def __init__(self, x, y, max_range):
        self.MAX_RANGE = max_range
        self.position = [x, y]
        self.new_position = None
        self.move = False

    def get_new_position(self):
        if self.position[1] == self.MAX_RANGE:
            self.new_position = [self.position[0], 0]
        else:
            self.new_position = [self.position[0], self.position[1] + 1]

    def check_move(self, cucumbers):
        self.get_new_position()
        if self.new_position not in cucumbers.south_positions and self.new_position not in cucumbers.east_positions:
            self.move = True

    def do_move(self):
        if self.move:
            self.position[0], self.position[1] = self.new_position
        self.move = False


with open('input.txt') as f:
    lines = f.read().splitlines()

cucumbers, east_cucumbers, south_cucumbers = Cucumbers(len(lines[0]), len(lines)), list(), list()


for y in range(len(lines)):
    for x in range(len(lines[0])):
        if lines[y][x] == '>':
            east_cucumbers.append(East_Cucumber(x, y, len(lines[0]) - 1))
            cucumbers.add_east_cucumber(east_cucumbers[-1])
        elif lines[y][x] == 'v':
            south_cucumbers.append(South_Cucumber(x, y, len(lines) - 1))
            cucumbers.add_south_cucumber(south_cucumbers[-1])

step = 0

while True:
    cucumbers.set_previous_state()
    for east_cucumber in east_cucumbers:
        east_cucumber.check_move(cucumbers)
    for east_cucumber in east_cucumbers:
        east_cucumber.do_move()
    for south_cucumber in south_cucumbers:
        south_cucumber.check_move(cucumbers)
    for south_cucumber in south_cucumbers:
        south_cucumber.do_move()
    if cucumbers.check_final_state():
        print(f'--- State after step {step + 1} ---')
        cucumbers.print_state()
        print('')
        print(f'Final state reached after {step + 1} steps')
        break
    step += 1
    print(f'Step {step} finished')