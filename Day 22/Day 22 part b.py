with open('input.txt') as f:
    lines = f.read().splitlines()

class Cube():
    def __init__(self, number, cube, toggle):
        self.number = number
        self.cube, self.toggle = cube, toggle

def cube_dimension(A):
    val = 1
    for i in range(3):
        val *= A[1][i] - A[0][i] + 1  # Endpoint shall be included!
    return val

def cube_A_in_B(A, B):
    for i in range(3):
        if not B[0][i] <= A[0][i] <= A[1][i] <= B[1][i]:
            return False
    return True

def cube_A_overlap_B(A, B):
    overlap = [None, None, None]  # Overlap in x, y, z
    count = 0
    for i in range(3):
        if B[0][i] <= A[0][i] <= B[1][i] and A[1][i] > B[1][i]:    # Start point overlap
            overlap[i] = (A[0][i], B[1][i])
        elif B[0][i] <= A[1][i] <= B[1][i] and A[0][i] < B[0][i]:  # End point overlap
            overlap[i] = (B[0][i], A[1][i])
        elif B[0][i] <= A[0][i] <= A[1][i] <= B[1][i]:             # slice B over A
            overlap[i] = (A[0][i], A[1][i])
            count += 1
        elif A[0][i] <= B[0][i] <= B[1][i] <= A[1][i]:             # slice A over B
            overlap[i] = (B[0][i], B[1][i])
    if None in overlap or count == 3:                              # If count is 3 --> A in B
        return None
    else:
        return (overlap[0][0], overlap[1][0], overlap[2][0]), (overlap[0][1], overlap[1][1], overlap[2][1])

def split_cube(A, B):
    sub_cubes = []
    x_y_z = [[], [], []]
    for i in range(3):
        # Three possibilities --> overlap from start (A0 == B0); overlap from end (A1 == B1) or overlap in middle (else)
        if A[0][i] == B[0][i] and A[1][i] != B[1][i]:
            x_y_z[i].append((A[0][i], B[1][i]))
            x_y_z[i].append((B[1][i] + 1, A[1][i]))
        elif A[1][i] == B[1][i] and A[0][i] != B[0][i]:
            x_y_z[i].append((A[0][i], B[0][i] - 1))
            x_y_z[i].append((B[0][i], A[1][i]))
        elif A[0][i] == B[0][i] and A[1][i] == B[1][i]:
            x_y_z[i].append((A[0][i], B[1][i]))
        else:
            x_y_z[i].append((A[0][i], B[0][i] - 1))
            x_y_z[i].append((B[0][i], B[1][i]))
            x_y_z[i].append((B[1][i] + 1, A[1][i]))
    for x in range(len(x_y_z[0])):
        for y in range(len(x_y_z[1])):
            for z in range(len(x_y_z[2])):
                start_point, end_point = (x_y_z[0][x][0], x_y_z[1][y][0], x_y_z[2][z][0]), (x_y_z[0][x][1], x_y_z[1][y][1], x_y_z[2][z][1])
                sub_cubes.append((start_point, end_point))
    return sub_cubes

cubes, cubes_list = dict(), list()

for i, line in enumerate(lines):
    x1, x2 = int(line.split('=')[1].split('..')[0]), int(line.split('..')[1].split(',')[0])
    y1, y2 = int(line.split('=')[2].split('..')[0]), int(line.split('..')[2].split(',')[0])
    z1, z2 = int(line.split('=')[3].split('..')[0]), int(line.split('..')[3])
    cube = ((min(x1, x2), min(y1, y2), min(z1, z2)), (max(x1, x2), max(y1, y2), max(z1, z2)))
    cubes[i + 1] = Cube(i + 1, cube, line.split(' ')[0])
    cubes_list.append(i + 1)

final_cubes = {cubes[cubes_list[-1]]}

for cube in reversed(cubes_list[:-1]):
    print(f'Analysing cube {cubes[cube].number}')
    to_analyse = {cubes[cube]}
    for cube_B in final_cubes.copy():
        current_analyse = to_analyse.copy()
        to_analyse = set()
        for cube_A in current_analyse:
            if cube_A_in_B(cube_A.cube, cube_B.cube):
                continue
            elif cube_A_in_B(cube_B.cube, cube_A.cube):
                splitted = split_cube(cube_A.cube, cube_B.cube)
                for split in splitted:
                    if split != cube_B.cube:
                        to_analyse.add(Cube('x', split, cube_A.toggle))
                continue
            overlap = cube_A_overlap_B(cube_A.cube, cube_B.cube)
            if overlap is not None:
                splitted = split_cube(cube_A.cube, overlap)
                for split in splitted:
                    if split != overlap:
                        to_analyse.add(Cube('x', split, cube_A.toggle))
                continue
            elif overlap is None:
                to_analyse.add(cube_A)
    for cube in to_analyse:
        final_cubes.add(cube)

answer_part_2 = 0
for cube in final_cubes:
    if cube.toggle == 'on':
        answer_part_2 += cube_dimension(cube.cube)

print(f'The answer to part 2 = {answer_part_2}')
