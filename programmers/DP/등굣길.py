def solution(col, row, puddles):
    dp = [[0 for _ in range(col)] for _ in range(row)]

    for c, r in puddles:
        dp[r - 1][c - 1] = -1

    # 첫 번째 행 초기화
    for c in range(col):
        if dp[0][c] == -1:  # 웅덩이를 만나면 이후는 경로가 없음
            break
        dp[0][c] = 1

    # 첫 번째 열 초기화
    for r in range(row):
        if dp[r][0] == -1:  # 웅덩이를 만나면 이후는 경로가 없음
            break
        dp[r][0] = 1

    for r in range(1, row):
        for c in range(1, col):
            if dp[r][c] == -1:
                continue
            elif dp[r - 1][c] == -1:
                dp[r][c] = dp[r][c - 1]
            elif dp[r][c - 1] == -1:
                dp[r][c] = dp[r - 1][c]
            else:
                dp[r][c] = (dp[r - 1][c] + dp[r][c - 1]) % 1000000007
    
    
    return dp[row - 1][col - 1]

print(solution(1, 2, []))