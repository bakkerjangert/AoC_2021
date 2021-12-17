from termcolor import colored

with open('input.txt') as f:
    lines = f.read().splitlines()

print_part_1 = True
print_part_2 = False

class Node():
    def __init__(self, position, max_x, max_y):
        self.position = position
        self.risk_level = max_x * max_y * 9  # Inital maximum possible value of total grid (h x w x 9)
        self.neighbours = []
        for delta in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            neighbour = (position[0] + delta[0], position[1] + delta[1])
            if 0 <= neighbour[0] < max_x and 0 <= neighbour[1] < max_y:
                self.neighbours.append(neighbour)
            else:
                continue   # Neigbor out of boundary
        self.to_be_visited_neighbours = self.neighbours.copy()
        self.previous_Node = None


def solve_maze(current_node, goal_node):
    step = 0
    while True:
        step += 1
        if step % 10000 == 0:
            print(f'At position {current_node.position} at step {step}')
        # Select neighbors
        neigbor_nodes = current_node.neighbours
        # Update risk level of neighbors
        risk_levels = []
        for neigbor_node in neigbor_nodes.copy():
            if nodes[neigbor_node] not in finished_nodes:
                next_potential_nodes.add(nodes[neigbor_node])
            new_risk_level = current_node.risk_level + maze[neigbor_node[1]][neigbor_node[0]]
            risk_levels.append(new_risk_level)
            if new_risk_level < nodes[neigbor_node].risk_level:
                nodes[neigbor_node].risk_level = new_risk_level
                nodes[neigbor_node].previous_Node = current_node.position
        # Choose next node
        if len(next_potential_nodes) == 0 or current_node.position == goal_node:
            break  # No more nodes to be processed
        max_risk_level = x_max * y_max * 9
        finished_nodes.add(current_node)
        for next_potential_node in next_potential_nodes:
            current_risk_level = next_potential_node.risk_level
            if current_risk_level < max_risk_level:
                max_risk_level = current_risk_level
                next_node = next_potential_node
        next_potential_nodes.remove(next_node)
        current_node = next_node
    return goal_node.risk_level

# Part 1
maze = []
for line in lines:
    maze.append(list(map(int, list(line))))
x_max, y_max = len(maze[0]), len(maze)

nodes = dict()
for x in range(len(maze[0])):
    for y in range(len(maze)):
        nodes[(x, y)] = Node((x, y), x_max, y_max)
        # print(f'{nodes[(x, y)].position} --> {nodes[(x, y)].neighbours} --> {nodes[(x, y)].risk_level}')

current_node = nodes[(0, 0)]
current_node.risk_level = 0
next_potential_nodes = set()
finished_nodes = set()
goal_node = nodes[(x_max - 1, y_max - 1)]

answer_part_1 = solve_maze(current_node, goal_node)

print(f'The answer to part 1 = {answer_part_1}')

if print_part_1:
    path = []
    cur_pos = goal_node.position

    while True:
        path.append(cur_pos)
        if nodes[cur_pos].previous_Node is None:
            break                                                       # Start node found
        cur_pos = nodes[cur_pos].previous_Node

    for y in range(y_max):
        for x in range(x_max):
            color = 'blue'
            if (x, y) in path:
                color = 'yellow'
            print(colored(maze[y][x], color), end='')
        print('')

# Part 2
maze_2 = []

for line in maze:
    maze_2.append([])
    colors = ['blue', 'red', 'yellow', 'white', 'green']
    for i in range(5):
        color = colors[i]
        for char in line.copy():
            next_val = (char + i - 1) % 9 + 1
            maze_2[-1].append(next_val)
    #         print(colored(next_val, color), end='')
    # print('')

for i in range(4):
    colors = colors[1:] + colors[:1]
    for j in range(0, len(maze)):
        maze_2.append([])
        line = maze_2[j + i * len(maze)].copy()
        col_index = 0
        for char in line:
            maze_2[-1].append(char % 9 + 1)
            color = colors[col_index // len(maze[0])]
            col_index += 1
        #     print(colored(maze_2[-1][-1], color), end='')
        # print('')

maze = maze_2
print(f'Grid size part 2 = {len(maze[0])} x {len(maze)}')
x_max, y_max = len(maze[0]), len(maze)
nodes = dict()
for x in range(len(maze[0])):
    for y in range(len(maze)):
        nodes[(x, y)] = Node((x, y), x_max, y_max)
        # print(f'{nodes[(x, y)].position} --> {nodes[(x, y)].neighbours} --> {nodes[(x, y)].risk_level}')

current_node = nodes[(0, 0)]
current_node.risk_level = 0
next_potential_nodes = set()
finished_nodes = set()
goal_node = nodes[(x_max - 1, y_max - 1)]

answer_part_2 = solve_maze(current_node, goal_node)

print(f'The answer to part 2 = {answer_part_2}')

if print_part_2:
    path = []
    cur_pos = goal_node.position

    while True:
        path.append(cur_pos)
        if nodes[cur_pos].previous_Node is None:
            break                                                       # Start node found
        cur_pos = nodes[cur_pos].previous_Node

    for y in range(y_max):
        for x in range(x_max):
            color = 'blue'
            if (x, y) in path:
                color = 'yellow'
            print(colored(maze[y][x], color), end='')
        print('')
