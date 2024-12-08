
antinodes = set()

grid = []

line = input()
while line != '':
    grid.append(list(line))
    line = input()

height = len(grid)
width = len(grid[0])

nodes = {}

for i in range(height):
    for j in range(width):
        if grid[i][j] != ".":
            if grid[i][j] in nodes:
                nodes[grid[i][j]].append((i, j))
            else:
                nodes[grid[i][j]] = [(i, j)]


def antinode(pr1, pr2):
    x1, y1 = pr1
    x2, y2 = pr2
    newx = x2 + (x2 - x1)
    newy = y2 + (y2 - y1)
    if newx >= 0 and newx < height and newy >= 0 and newy < width:
        antinodes.add((newx, newy))


for k in nodes:
    node_list = nodes[k]
    L = len(node_list)
    for i in range(L):
        for j in range(i):
            node1 = node_list[i]
            node2 = node_list[j]
            antinode(node1, node2)
            antinode(node2, node1)

print(len(antinodes))
