from itertools import product


def find_total(numbers, operators):
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i+1]
        elif op == '*':
            result *= numbers[i+1]
    return result


def can_find_total(total, numbers):
    n = len(numbers) - 1
    for ops in product(['+', '*'], repeat=n):
        if find_total(numbers, ops) == total:
            return True
    return False


line = input()
suma = 0
while line != '':
    sections = line.strip().split(': ')
    total = int(sections[0])
    numbers = list(int(_) for _ in sections[1].split(' '))
    if can_find_total(total, numbers):
        suma += total
    line = input()
print(suma)
