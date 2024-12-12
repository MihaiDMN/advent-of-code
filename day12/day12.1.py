import numpy as np


def find_plots(grid):
    rows, cols = grid.shape
    visited = [[False] * cols for _ in range(rows)]

    def neighbours(row, cols):
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = row + dr, cols + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                yield nr, nc

    def calculate(row, col):
        plant = grid[row, col]
        stack = [(row, col)]
        area = 0
        perimeter = 0

        while stack:
            x, y = stack.pop()
            area += 1
            for nr, nc in neighbours(x, y):
                if grid[nr, nc] == plant:
                    if not visited[nr][nc]:
                        visited[nr][nc] = True
                        stack.append((nr, nc))
                else:
                    perimeter += 1
                perimeter += sum(1 for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]
                                 if not (0 <= x + dr < rows and 0 <= y + dc < cols))
        return area, perimeter

    total = 0

    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                area, perimeter = calculate(r, c)
                print(area, perimeter)
                total += area * perimeter

    return total


line = input()
text = ''
while line != '':
    text += line + '\n'
    line = input()

grid = np.array([list(row) for row in text.strip().split('\n')])
print(find_plots(grid))