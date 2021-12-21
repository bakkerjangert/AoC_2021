from copy import deepcopy

class Player():
    def __init__(self, position, name):
        self.name = name
        self.position = position
        self.score = 0
        self.rolls = []


# players = [Player(4, 'Player 1'), Player(8, 'Player 2')]  # Test input
players = [Player(6, 'Player 1'), Player(10, 'Player 2')]
turn, throws = 0, 0
dice_number = 1
while True:
    player = players[turn % 2]
    delta = 0
    for i in range(3):
        delta += dice_number
        if dice_number < 100:
            dice_number += 1
        else:
            dice_number = 1
    turn += 1
    throws += 3
    new_position = (player.position + delta) % 10
    if new_position == 0:
        new_position = 10
    # print(f'{player.name} throws {delta} going from {player.position} to {new_position} --> total score = {player.score + new_position}')
    # input('Pause...')
    player.position = new_position
    player.score += new_position
    if player.score >= 1000:
        print(f'The answer to part 1 = {players[turn % 2].score} x {throws} = {players[turn % 2].score * throws}')
        break

base = (1, 1, 1)
data = []

throws = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}


player_1_ongoing, player_2_ongoing = dict(), dict()
player_1_finished, player_2_finished = dict(), dict()

player_1_ongoing[0], player_2_ongoing[0] = [Player(4, 'Player 1')], [Player(8, 'Player 2')]  # Test input
# player_1_ongoing[0], player_2_ongoing[0] = [Player(6, 'Player 1')], [Player(10, 'Player 2')]

# Player 1
turn = 1
while True:
    player_1_ongoing[turn] = []
    for player in player_1_ongoing[turn - 1]:
        for throw in throws.keys():
            player_copy = deepcopy(player)
            new_position = (player_copy.position + throw) % 10
            if new_position == 0:
                new_position = 10
            player_copy.position = new_position
            player_copy.score += new_position
            player_copy.rolls.append(throw)
            if player_copy.score >= 21:
                if turn not in player_1_finished.keys():
                    player_1_finished[turn] = []
                player_1_finished[turn].append(player_copy)
            else:
                player_1_ongoing[turn].append(player_copy)
    if len(player_1_ongoing[turn]) == 0:
        del player_1_ongoing[turn]
        break
    turn += 1

# Player 2
turn = 1
while True:
    player_2_ongoing[turn] = []
    for player in player_2_ongoing[turn - 1]:
        for throw in throws.keys():
            player_copy = deepcopy(player)
            new_position = (player_copy.position + throw) % 10
            if new_position == 0:
                new_position = 10
            player_copy.position = new_position
            player_copy.score += new_position
            player_copy.rolls.append(throw)
            if player_copy.score >= 21:
                if turn not in player_2_finished.keys():
                    player_2_finished[turn] = []
                player_2_finished[turn].append(player_copy)
            else:
                player_2_ongoing[turn].append(player_copy)
    if len(player_2_ongoing[turn]) == 0:
        del player_2_ongoing[turn]
        break
    turn += 1

for key in player_2_ongoing.keys():
    print(f'At round {key} there are {len(player_2_ongoing[key])} players 2 ongoing')

for key in player_2_finished.keys():
    print(f'At round {key} there are {len(player_2_finished[key])} players 2 finished')
# Player 1 wins at [turn] --> Player 2 ongoing at [turn - 1]
# Player 2 wins at [turn] --> Player 1 ongoing at [turn]

wins_player_1 = 0
for turn in player_1_finished.keys():
    for player_1 in player_1_finished[turn]:
        for player_2 in player_2_ongoing[turn - 1]:
            realities = 1
            for number in player_1.rolls:
                realities *= throws[number]
            for number in player_2.rolls:
                realities *= throws[number]
            wins_player_1 += realities
print(f'Player 1 wins {wins_player_1} times')

wins_player_2 = 0
for turn in player_2_finished.keys():
    for player_2 in player_2_finished[turn]:
        for player_1 in player_1_ongoing[turn]:
            realities = 1
            for number in player_2.rolls:
                realities *= throws[number]
            for number in player_1.rolls:
                realities *= throws[number]
            wins_player_2 += realities
print(f'Player 2 wins {wins_player_2} times')
print(f'The answer to part 2 = {min(wins_player_1, wins_player_2)}')
