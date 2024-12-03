import re


pattern = r"mul\((\d{1,3}),(\d{1,3})\)"


line = input()
total = 0
while line != '':
    matches = re.findall(pattern, line)
    line = input()
    for match in matches:
        total += int(match[0]) * int(match[1])

print(total)
