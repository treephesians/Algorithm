# https://www.acmicpc.net/problem/9251

import sys

input = sys.stdin.readline

# ACAYKP
# CAPCAK
#     -    A    C    A    Y    K    P
# -   0    0    0    0    0    0    0
# C   0    0    1    1    1    1    1
# A   0    1    1    2    2    2    2
# P   0    1    1    2    2    2    3
# C   0    1    2    2    2    2    3
# A   0    1    2    3    3    3    3
# K   0    1    2    3    3    4    4

arr = []
for _ in range(2):
    arr.append([c for c in input().strip()])

l1 = len(arr[0])
l2 = len(arr[1])

dp = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]

for i in range(1, l1 + 1):
    for j in range(1, l2 + 1):
        if arr[0][i - 1] == arr[1][j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

print(dp[l1][l2])