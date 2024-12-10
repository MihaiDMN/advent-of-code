import sys

input = sys.stdin.read().strip()
grid = [[int(h) for h in _] for _ in input.split("\n")]


def grid_value(x, y):
    if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
        return grid[x][y]
    return -1


def get_trails(grid, x, y):
    trails = set()
    height = grid[x][y]
    if height == 9:
        trails.add((x, y))
        return trails
    if grid_value(x+1, y) == height+1:
        trails.update(get_trails(grid, x+1, y))
    if grid_value(x-1, y) == height+1:
        trails.update(get_trails(grid, x-1, y))
    if grid_value(x, y+1) == height+1:
        trails.update(get_trails(grid, x, y+1))
    if grid_value(x, y-1) == height+1:
        trails.update(get_trails(grid, x, y-1))
    return trails


total = 0

for x, row in enumerate(grid):
    for y, height in enumerate(row):
        if grid[x][y] == 0:
            score = len(get_trails(grid, x, y))
            total += score
print(total)
