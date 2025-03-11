import sys
input = sys.stdin.readline

N, K = map(int, input().split())
DP = [0 for _ in range(K + 1)]

for _ in range(N):
    W, V = map(int, input().split())
    for j in range(K, W - 1, -1):  # 뒤에서부터 계산해야 이전 값 안 덮어씀
        DP[j] = max(DP[j], DP[j - W] + V)

print(max(DP))  # DP[K]가 아니라 max(DP)여도 됩니다