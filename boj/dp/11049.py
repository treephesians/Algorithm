import sys
input = sys.stdin.readline

# 입력 처리
N = int(input())
matrices = [tuple(map(int, input().split())) for _ in range(N)]

# DP 테이블 초기화
dp = [[0] * N for _ in range(N)]

# DP 계산
for length in range(1, N):  # 길이: 2부터 N까지
    for i in range(N - length):
        j = i + length
        dp[i][j] = float('inf')
        for k in range(i, j):
            cost = dp[i][k] + dp[k+1][j] + matrices[i][0] * matrices[k][1] * matrices[j][1]
            dp[i][j] = min(dp[i][j], cost)

# 결과 출력
print(dp[0][N-1])