import sys
input = sys.stdin.readline

# 입력
N, M = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))

# DP 배열 초기화
max_cost = sum(cost)  # 모든 비용의 합 (최대 비용)
dp = [0] * (max_cost + 1)  # dp[c]: 비용 c로 확보할 수 있는 최대 메모리

# 동적 계획법
for i in range(N):
    m_i, c_i = memory[i], cost[i]
    for c in range(max_cost, c_i - 1, -1):  # 뒤에서부터 업데이트
        dp[c] = max(dp[c], dp[c - c_i] + m_i)

# 최소 비용 찾기
for c in range(max_cost + 1):
    if dp[c] >= M:
        print(c)
        break