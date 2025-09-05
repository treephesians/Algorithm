def solution(info, n, m):
    length = len(info)
    dp = [[[False]*m for _ in range(n)]for _ in range(length+1)]
    dp[0][0][0] = True
    for day in range(length):
        for a in range(n):
            for b in range(m):
                if dp[day][a][b] == False: continue
                if a + info[day][0] < n: dp[day+1][a+info[day][0]][b] = True
                if b + info[day][1] < m: dp[day+1][a][b+info[day][1]] = True
    for i in range(n):
        for j in range(m):
            if dp[length][i][j]: return i
    return -1

info = [[3, 3], [3, 3]]
n = 6
m = 1
print(solution(info, n, m))
