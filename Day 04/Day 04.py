from termcolor import colored
with open('input.txt') as f:
    lines = f.read().splitlines()


class BingoCard():
    def __init__(self, number_lines, card_number):
        self.card_number = card_number
        self.card = []
        for line in number_lines:
            if line[0] == ' ':
                line = line[1:]
            self.card += list(map(int, line.replace('  ', ' ').split(' ')))
        self.checker = [1] * 25  # 1 if number not drawn; 0 if number is drawn
        self.winning_card = False

    def draw_number(self, number):
        if number in self.card:
            self.checker[self.card.index(number)] = 0
            self.check_card()

    def check_card(self):
        # Check horizontal lines
        for i in range(0, 25, 5):
            if not (1 in self.checker[i: i + 5]):
                self.winning_card = True
                return True
        # Check vertical lines
        for i in range(5):
            val = []
            for j in range(5):
                val.append(self.checker[i + j * 5])
            if not (1 in val):
                self.winning_card = True
                return True

    def calculate_sum(self):
        numbers = list(map(int, self.card))
        return sum([numbers[i] * self.checker[i] for i in range(len(numbers))])

    def print_card(self):
        print(f'--- Printing current state of Card No {self.card_number} ----')
        for i in range(25):
            if self.checker[i] == 0:
                color = 'yellow'
            else:
                color = 'blue'
            if self.card[i] < 10:
                print(' ', end='')
            print(colored(self.card[i], color) + ' ', end='')
            if (i + 1) % 5 == 0:
                print('')


number_of_cards = len(lines) // 6
draws = list(map(int, lines[0].split(',')))
bingo_cards = []

for i in range(number_of_cards):
    bingo_cards.append(BingoCard(lines[2 + i * 6: 7 + i * 6], i + 1))

first_winning_card = True
last_winning_card = False
for number in draws:
    for card in bingo_cards.copy():
        card.draw_number(number)
        if card.winning_card:
            if first_winning_card:
                print(f'The answer to part 1 = Card {card.card_number} won with {number} x {card.calculate_sum()} = '
                      f'{int(number) * card.calculate_sum()} points:')
                first_winning_card = False
                card.print_card()
                print('')
            if len(bingo_cards) == 1:
                last_winning_card = True
                print(f'The answer to part 2 = Card {card.card_number} loses with {number} x {card.calculate_sum()} = '
                      f'{int(number) * card.calculate_sum()} points:')
                card.print_card()
            bingo_cards.remove(card)
    if last_winning_card:
        break


# for i in range(len(bingo_cards)):
#     print(f'\n--- CARD {i+1} ---\n')
#     bingo_cards[i].print_card()