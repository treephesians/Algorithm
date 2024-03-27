import sys

T = int(sys.stdin.readline())

dp = [0, 1, 2, 4]

for _ in range(T):
    n = int(sys.stdin.readline())
    l = len(dp) - 1
    if l < n:
        for i in range(n - l):
            dpn = dp[l + i] + dp[l + i - 1] + dp[l + i - 2]
            dp.append(dpn)
    print(dp[n])