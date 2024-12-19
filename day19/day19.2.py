import sys


def count_ways(patterns, towel, memo=None):
    if memo is None:
        memo = {}
    if towel in memo:
        return memo[towel]
    if towel == "":
        return 1

    total_ways = 0
    for pattern in patterns:
        if towel.startswith(pattern):
            total_ways += count_ways(patterns, towel[len(pattern):], memo)

    memo[towel] = total_ways
    return total_ways


input = sys.stdin.read()
patterns_list = []
total = 0
patterns = input.strip().split('\n\n')[0]
towels = input.strip().split('\n\n')[1]
patterns_list = patterns.split(', ')
towels_list = towels.split('\n')
for towel in towels_list:
    total += count_ways(patterns_list, towel)
print(total)
