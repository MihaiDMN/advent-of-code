import sys


def is_design_possible_dp(patterns, towel):
    n = len(towel)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for pattern in patterns:
            if i >= len(pattern) and towel[i - len(pattern):i] == pattern:
                dp[i] = dp[i] or dp[i - len(pattern)]
                if dp[i]:
                    break

    return dp[n]


input = sys.stdin.read()
patterns_list = []
total = 0
patterns = input.strip().split('\n\n')[0]
towels = input.strip().split('\n\n')[1]
patterns_list = patterns.split(', ')
towels_list = towels.split('\n')
for towel in towels_list:
    if is_design_possible_dp(patterns_list, towel):
        total += 1
print(total)
