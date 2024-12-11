# https://www.acmicpc.net/problem/9465
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    arr = []
    n = int(input())
    for _ in range(2):
        arr.append(list(map(int, input().split())))
    dp = [[arr[0][0], arr[1][0] + arr[0][1]], [arr[1][0], arr[0][0] + arr[1][1]]]

    for i in range(2, n):
        dp[0].append(max(dp[1][i - 2], dp[1][i - 1]) + arr[0][i])
        dp[1].append(max(dp[0][i - 2], dp[0][i - 1]) + arr[1][i]) 
    
    print(max(dp[0][n - 1], dp[1][n - 1]))