import sys

N = int(sys.stdin.readline())

arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))


dp = [[0 for _ in range(N)] for _ in range(2)]
result = 0

if N == 1:
    result = arr[0]
elif N == 2:
    result = arr[0] + arr[1]
else:
    dp[0][0] = arr[0]
    dp[0][1] = arr[1]
    dp[1][1] = arr[0] + arr[1]

    for i in range(2, N):
        dp[0][i] = max(dp[0][i - 2], dp[1][i - 2]) + arr[i]
        dp[1][i] = dp[0][i - 1] + arr[i]

    result = max(dp[0][N - 1], dp[1][N - 1])

print(result)