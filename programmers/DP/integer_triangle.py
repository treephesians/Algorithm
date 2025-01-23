def solution(triangle):
    size = len(triangle)
    dp = [[0 for _ in range(size)] for _ in range(size)]
    dp[0][0] = triangle[0][0]
    
    for i in range(1, size):
        for j in range(i + 1):
            if j == 0:
                dp[i][j] = dp[i - 1][0] + triangle[i][0]
            elif j < i:
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
            else:
                dp[i][j] = dp[i - 1][i - 1] + triangle[i][i]
    
    answer = max(dp[size - 1])
    
    return answer