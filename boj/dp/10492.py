# https://www.acmicpc.net/problem/10942

import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp = [[-1 for _ in range(N)] for _ in range(N)]

for n in range(N):
    dp[n][n] = 1

for col in range(1, N):
    for row in range(0, col):
        if arr[col] == arr[row] and col != row:
            if dp[row + 1][col - 1] != 0:
                dp[row][col] = 1
            else:
                dp[row][col] = 0
        else:
            dp[row][col] = 0

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(dp[a - 1][b - 1])