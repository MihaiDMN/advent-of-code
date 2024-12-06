import numpy as np


def track_map(grid):
    directions = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
    position = None
    direction = None

    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell in directions:
                position = (r, c)
                direction = directions[cell]
                grid[r][c] = '.'
                break
        if position:
            break
    return grid, position, direction


def move(grid, position, direction):
    directions = [
        (-1, 0),  # Up
        (0, 1),   # Right
        (1, 0),   # Down
        (0, -1),  # Left
    ]
    direction_index = directions.index(direction)
    visited = set()
    current_position = position

    rows, cols = len(grid), len(grid[0])
    while True:
        visited.add(current_position)
        r, c = current_position
        dr, dc = directions[direction_index]
        new_position = (r + dr, c + dc)
        if not (0 <= new_position[0] < rows and 0 <= new_position[1] < cols):
            break
        if grid[new_position[0]][new_position[1]] == '#':
            direction_index = (direction_index + 1) % 4
        else:
            current_position = new_position

    return visited


line = input()
text = ''
total = 0
while line != '':
    text += line + '\n'
    line = input()
# pip install numpy if you don't have it
grid = np.array([list(row) for row in text.strip().split('\n')])
grid, position, direction = track_map(grid)
visited = move(grid, position, direction)
total = len(set(visited))

print(total)
