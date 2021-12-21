from copy import deepcopy
import time

start = time.time()

with open('input.txt') as f:
    lines = f.read().splitlines()


masks = (('+1x', '+1y', '+1z'), ('+1x', '-1z', '+1y'), ('+1x', '-1y', '-1z'), ('+1x', '+1z', '-1y'),
         ('+1y', '-1x', '+1z'), ('+1y', '+1z', '+1x'), ('+1y', '+1x', '-1z'), ('+1y', '-1z', '-1x'),
         ('-1x', '-1y', '+1z'), ('-1x', '+1z', '+1y'), ('-1x', '+1y', '-1z'), ('-1x', '-1z', '-1y'),
         ('-1y', '+1x', '+1z'), ('-1y', '-1z', '+1x'), ('-1y', '-1x', '-1z'), ('-1y', '+1z', '-1x'),
         ('+1z', '+1y', '-1x'), ('+1z', '+1x', '+1y'), ('+1z', '-1y', '+1x'), ('+1z', '-1x', '-1y'),
         ('-1z', '+1y', '+1x'), ('-1z', '+1x', '-1y'), ('-1z', '-1y', '-1x'), ('-1z', '-1x', '+1y'))

deltas = {'x': 0, 'y': 1, 'z': 2}

class Scanner():
    def __init__(self, name):
        self.name = name
        self.scanner = [0, 0, 0]
        self.beacons = []
        self.range_min, self.range_max = [-1000, -1000, -1000], [1000, 1000, 1000]
        self.not_in_range = []
        self.manhattan_distances = set()
        self.found_position = False

    def shift(self, delta):
        for i in range(3):
            self.scanner[i] += delta[i]
            self.range_min[i] += delta[i]
            self.range_max[i] += delta[i]
            for beacon in self.beacons:
                beacon[i] += delta[i]

    def rotate(self, rotation):
        new_scanner, new_min, new_max = [], [], []
        for i in range(3):
            new_scanner.append(int(rotation[i][:2]) * self.scanner[deltas[rotation[i][2]]])
            new_min.append(int(rotation[i][:2]) * self.range_min[deltas[rotation[i][2]]])
            new_max.append(int(rotation[i][:2]) * self.range_max[deltas[rotation[i][2]]])
        self.scanner = new_scanner
        for i in range(3):
            self.range_min[i], self.range_max[i] = min(new_min[i], new_max[i]), max(new_min[i], new_max[i])
        new_beacons = []
        for beacon in self.beacons:
            new_beacon = []
            for i in range(3):
                new_beacon.append(int(rotation[i][:2]) * beacon[deltas[rotation[i][2]]])
            new_beacons.append(new_beacon)
        self.beacons = new_beacons

    def manhatan(self):
        for i in range(len(self.beacons) - 1):
            for j in range(i + 1, len(self.beacons)):
                distance = 0
                for k in range(3):
                    distance += abs(self.beacons[i][k] - self.beacons[j][k])
                self.manhattan_distances.add(distance)

scanners, finished_scanners = list(), list()
name = None
for line in lines:
    if '---' in line:
        name = line.split(' ')[1] + ' ' + line.split(' ')[2]
        scanners.append(Scanner(name))
    elif ',' in line:
        scanners[-1].beacons.append(list(map(int, line.split(','))))
for scanner in scanners:
    scanner.manhatan()

finished_scanners.append(scanners.pop(0))
finished_scanners[0].found_position = True

while len(scanners) > 0:
    for scanner in scanners:
        print(f'--- Analysing {scanner.name} ---')
        scanner_finished = False
        for target_scanner in finished_scanners:
            if target_scanner.name in scanner.not_in_range:
                continue
            if scanner_finished:
                break
            count = 0
            for manhattan_distance in scanner.manhattan_distances:
                if manhattan_distance in target_scanner.manhattan_distances:
                    count += 1
            if count < 11 + 10 + 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1:
                scanner.not_in_range.append(target_scanner.name)
                continue
            for mask in masks:
                if scanner_finished:
                    break
                # print(f'compare to {target_scanner.name} with rotation {mask}')
                for i in range(len(scanner.beacons)):
                    for j in range(len(target_scanner.beacons)):
                        if scanner_finished:
                            break
                        copy_1 = deepcopy(scanner)
                        copy_1.rotate(mask)
                        shift = []
                        for index in range(3):
                            shift.append(target_scanner.beacons[j][index] - copy_1.beacons[i][index])
                        # print(f'shift beacon {copy_1.beacons[i]} to {target_scanner.beacons[j]}')
                        copy_2 = deepcopy(copy_1)
                        copy_2.shift(shift)
                        # print(f'shifted beacon is {copy_2.beacons[i]}')
                        # input('Pause ...')
                        count_beacons = 0
                        valid = True
                        for beacon in copy_2.beacons:
                            if target_scanner.range_min[0] <= beacon[0] <= target_scanner.range_max[0]:
                                if target_scanner.range_min[1] <= beacon[1] <= target_scanner.range_max[1]:
                                    if target_scanner.range_min[2] <= beacon[2] <= target_scanner.range_max[2]:
                                        # Beacon within target range
                                        # print(f'Beacon in range!')
                                        if beacon in target_scanner.beacons:
                                            count_beacons += 1
                                        else:
                                            valid = False
                                            break
                        # print(f'counted {count_beacons} valid beacons')
                        if valid and count_beacons >= 12:
                            print(f'Position of {scanner.name} found! Postion {copy_2.scanner} and rotation {mask};'
                                  f'min_range = {copy_2.range_min}; max_range = {copy_2.range_max}')
                            scanners.remove(scanner)
                            copy_2.found_position = True
                            finished_scanners.append(copy_2)
                            scanner_finished = True
                            break
            scanner.not_in_range.append(target_scanner.name)


beacon_set = set()

for scanner in finished_scanners:
    for beacon in scanner.beacons:
        beacon_set.add(tuple(beacon))

print(f'The answer to part 1 = {len(beacon_set)}')

answer_part_2 = 0
for i in range(len(finished_scanners)):
    for j in range(len(finished_scanners)):
        coord_1 = finished_scanners[i].scanner
        coord_2 = finished_scanners[j].scanner
        manhattan = 0
        for k in range(3):
            manhattan += abs(coord_1[k] - coord_2[k])
        if manhattan > answer_part_2:
            answer_part_2 = manhattan

end = time.time()

print(f'The answer to part 2 = {answer_part_2}')
print(f'Finished in {end - start} seconds')
