import re


pattern = r'mul\([0-9]{1,3},[0-9]{1,3}\)|(?:do\(\)|don\'t\(\))'
number_pattern = r"\d{1,3}"

line = input()
total = 0
do = True
while line != '':
    matches = re.findall(pattern, line)
    for match in matches:
        if match == "do()":
            do = True
        elif match == "don't()":
            do = False
        else:
            if do:
                numbers = re.findall(number_pattern, match)
                total += int(numbers[0]) * int(numbers[1])
    line = input()

print(total)
