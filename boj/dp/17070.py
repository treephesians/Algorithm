N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

dp = [[[0]*3 for _ in range(N)] for _ in range(N)]
dp[0][1][0] = 1  # 초기 상태: 가로로 (0,1)에 위치

for r in range(N):
    for c in range(N):
        if graph[r][c] == 1:
            continue
        # 가로
        if c-1 >= 0:
            dp[r][c][0] += dp[r][c-1][0] + dp[r][c-1][1]
        # 세로
        if r-1 >= 0:
            dp[r][c][2] += dp[r-1][c][2] + dp[r-1][c][1]
        # 대각선
        if r-1 >= 0 and c-1 >= 0:
            if graph[r-1][c] == 0 and graph[r][c-1] == 0:
                dp[r][c][1] += sum(dp[r-1][c-1])

print(sum(dp[N-1][N-1]))