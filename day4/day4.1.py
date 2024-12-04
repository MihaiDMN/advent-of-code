def count_xmas_occurrences(grid):
    def search_word(x, y, dx, dy):
        word = "XMAS"
        n = len(word)
        for i in range(n):
            nx, ny = x + i * dx, y + i * dy
            if not (0 <= nx < len(grid) and
                    0 <= ny < len(grid[0]) and
                    grid[nx][ny] == word[i]):
                return False
        return True

    directions = [
        (0, 1),   # Horizontal right
        (0, -1),  # Horizontal left
        (1, 0),   # Vertical down
        (-1, 0),  # Vertical up
        (1, 1),   # Diagonal down-right
        (-1, -1),  # Diagonal up-left
        (1, -1),  # Diagonal down-left
        (-1, 1),  # Diagonal up-right
    ]

    count = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            for dx, dy in directions:
                if search_word(x, y, dx, dy):
                    count += 1
    return count


line = input()
text = ''
while line != '':
    text += line + '\n'
    line = input()

grid = text.strip().split('\n')
result = count_xmas_occurrences(grid)
print(result)
