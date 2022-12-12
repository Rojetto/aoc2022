f = open("12.txt", "r")

height_map = []
start = (0, 0)
end = (0, 0)

for r, line in enumerate(f):
    row = []
    for c, char in enumerate(line):
        if char.islower():
            row.append(ord(char) - ord('a'))
        else:
            if char == "S":
                row.append(0)
                start = (r, c)
            elif char == "E":
                row.append(25)
                end = (r, c)

    height_map.append(row)


class path_node:
    def __init__(self, position, g_score, parent):
        self.position = position
        self.g_score = g_score
        self.parent = parent
        self.h_score = abs(position[0] - end[0]) + abs(position[1] - end[1])
    
    @property
    def f_score(self):
        return self.g_score + self.h_score

    def __eq__(self, other):
        return self.position == other.position

    def __hash__(self):
        return hash(self.position)


all_nodes = {}

def get_node(position):
    if position not in all_nodes:
        all_nodes[position] = path_node(position, 0, None)
    return all_nodes[position]
    

# A* search

open_set = set([path_node(start, 0, None)])
closed_set = set()

while open_set:
    current = min(open_set, key=lambda x: x.f_score)
    open_set.remove(current)
    closed_set.add(current)

    if current.position == end:
        break

    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        new_position = (current.position[0] + dx, current.position[1] + dy)
        if new_position[0] < 0 or new_position[0] >= len(height_map) or new_position[1] < 0 or new_position[1] >= len(height_map[0]):
            continue

        if height_map[new_position[0]][new_position[1]] - height_map[current.position[0]][current.position[1]] > 1:  # too high, only down or up one level
            continue

        new_node = get_node(new_position)
        if new_node in closed_set:
            continue

        new_g_score = current.g_score + 1
        if new_node not in open_set or new_g_score < new_node.g_score:
            new_node.parent = current
            new_node.g_score = new_g_score
            if new_node not in open_set:
                open_set.add(new_node)

# reconstruct path
path = []
while current:
    path.append(current.position)
    current = current.parent

path.reverse()
print("Path length:", len(path) - 1)
