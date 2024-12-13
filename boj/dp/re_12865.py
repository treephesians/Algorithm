# https://www.acmicpc.net/problem/12865

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
items = []
for _ in range(N):
    w, v = map(int, input().split())
    items.append((w, v))

dp = [0] * (K + 1)  # dp[w] = 무게 w까지 담을 때 얻을 수 있는 최대 가치

for w, v in items:
    # K부터 w까지 역순으로 순회
    for cur_w in range(K, w-1, -1):
        # 물건을 담는 경우와 담지 않는 경우를 비교
        dp[cur_w] = max(dp[cur_w], dp[cur_w - w] + v)

print(dp[K])  # dp[K] = 무게 K 이하로 담을 수 있는 최대 가치


# 5 11
# 6 13
# 4 8
# 3 6
# 5 9
# 4 9