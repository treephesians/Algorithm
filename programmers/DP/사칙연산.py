def solution(arr):
    n = (len(arr) + 1) // 2  # 숫자의 개수
    # DP 테이블 초기화
    dp_max = [[0] * n for _ in range(n)]
    dp_min = [[0] * n for _ in range(n)]
    
    # 초기값 설정
    for i in range(n):
        dp_max[i][i] = int(arr[2 * i])
        dp_min[i][i] = int(arr[2 * i])

    # DP 점화식 계산
    for length in range(1, n):  # 부분 구간의 길이
        for i in range(n - length):
            j = i + length
            dp_max[i][j] = float('-inf')
            dp_min[i][j] = float('inf')
            for k in range(i, j):  # i~j를 k로 나눔
                operator = arr[2 * k + 1]  # 연산자
                if operator == '+':
                    dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] + dp_max[k+1][j])
                    dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] + dp_min[k+1][j])
                elif operator == '-':
                    dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] - dp_min[k+1][j])
                    dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] - dp_max[k+1][j])

    return dp_max[0][n-1]