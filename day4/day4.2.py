import numpy as np


def search(grid, pos):
    x, y = pos
    if grid[x, y] != 'A':
        return False

    top_left = grid[x - 1, y - 1]
    top_right = grid[x - 1, y + 1]
    bottom_left = grid[x + 1, y - 1]
    bottom_right = grid[x + 1, y + 1]

    if top_left == 'M' and top_right == 'M' and bottom_right == 'S' and bottom_left == 'S':
        return True
    if top_left == 'S' and top_right == 'S' and bottom_right == 'M' and bottom_left == 'M':
        return True
    if top_left == 'S' and top_right == 'M' and bottom_right == 'M' and bottom_left == 'S':
        return True
    if top_left == 'M' and top_right == 'S' and bottom_right == 'S' and bottom_left == 'M':
        return True
    return False


line = input()
text = ''
total = 0
while line != '':
    text += line + '\n'
    line = input()
# pip install numpy if you don't have it
# I am manipulating the text to make it a numpy array to make it easiear to search for the pattern
grid = np.array([list(row) for row in text.strip().split('\n')])
x, y = grid.shape
total = 0

for row in range(1, y-1):
    for col in range(1, x-1):
        if search(grid, (col, row)):
            total += 1

print(total)
