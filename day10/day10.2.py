import sys
from copy import copy


class Trail:
    def __init__(self, path: list):
        self.path = path

    def add_step(self, x, y):
        self.path.append((x, y))


class Step:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.height = grid[x][y]


input = sys.stdin.read().strip()
grid = [[int(h) for h in _] for _ in input.split("\n")]


def grid_value(x, y):
    if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
        return grid[x][y]
    return -1


def find_unique_trails(grid, trail):
    trails = set()
    height = trail.path[-1].height
    x, y = trail.path[-1].x, trail.path[-1].y
    if height == 9:
        trails.add((trail))
        return trails
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if grid_value(nx, ny) == height + 1:
            new_trails = copy(trails)
            new_trails.add_step(x, y)
            trails.update(find_unique_trails(grid, new_trails))
    return trails


total = 0

for x, row in enumerate(grid):
    for y, height in enumerate(row):
        if grid[x][y] == 0:
            score = len(find_unique_trails(grid, Trail([Step(x, y)])))
            total += score
print(total)
