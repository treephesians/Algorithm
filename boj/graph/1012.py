import sys

t = int(sys.stdin.readline())

for _ in range(t):
    # 세팅
    answer = 0
    m, n, k = map(int, sys.stdin.readline().split()) # m은 가로, n이 세로
    matrix = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        _m, _n = map(int, sys.stdin.readline().split())
        matrix[_n][_m] = 1

    # BFS
    for row in range(n):
        for col in range(m):
            if matrix[row][col] == 1:
                answer += 1
                q = [[row, col]]
                while q:
                    _row, _col = q.pop(0)
                    if matrix[_row][_col] == 1:
                        matrix[_row][_col] = 0
                        # 4가지 방향 넣기
                        if _row + 1 < n and matrix[_row + 1][_col] == 1:
                            q.append([_row + 1, _col])
                            matrix[_row][_col] = 0
                        if _row - 1 >= 0 and matrix[_row - 1][_col] == 1:
                            q.append([_row - 1, _col])
                            matrix[_row][_col] = 0
                        if _col + 1 < m and matrix[_row][_col + 1] == 1:
                            q.append([_row, _col + 1])
                            matrix[_row][_col] = 0
                        if _col - 1 >= 0 and matrix[_row][_col - 1] == 1:
                            q.append([_row, _col - 1])
                            matrix[_row][_col] = 0
    print(answer)