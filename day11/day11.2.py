from collections import Counter
"""
--- Part Two ---
Instead of making a new list, this tracks the number
of occurences of each stone number in a Counter object.
For each unique stone number, we apply the blink rules.
"""


def blink(stones):
    new_stones = Counter()
    for num, count in stones.items():
        if num == 0:
            new_stones[1] += count
        elif len(str(num)) % 2 == 0:
            power = len(str(num)) // 2
            divisor = 10 ** power
            first_half = num // divisor
            second_half = num % divisor
            new_stones[first_half] += count
            new_stones[second_half] += count
        else:
            new_stones[num * 2024] += count
    return new_stones


line = input()

numbers = [int(x) for x in line.split(" ")]
stone_counter = Counter(numbers)
cnt = 0
while cnt < 75:
    print("Blinking", cnt)
    stone_counter = blink(stone_counter)
    cnt += 1
print(sum(stone_counter.values()))
