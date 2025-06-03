# 얘는 쉬운 DP문제이지만 공간복잡도를 고려해줘야하는 좋은 문제였다.

import sys

input = sys.stdin.readline

def solution(N, matrix, order):
    prev = matrix[0][:]  # 첫 줄 복사

    for i in range(1, N):
        curr = [0, 0, 0]
        if order == "max":
            curr[0] = matrix[i][0] + max(prev[0], prev[1])
            curr[1] = matrix[i][1] + max(prev[0], prev[1], prev[2])
            curr[2] = matrix[i][2] + max(prev[1], prev[2])
        else:  # min
            curr[0] = matrix[i][0] + min(prev[0], prev[1])
            curr[1] = matrix[i][1] + min(prev[0], prev[1], prev[2])
            curr[2] = matrix[i][2] + min(prev[1], prev[2])
        
        prev = curr  # 다음 루프를 위해 prev 갱신

    return max(prev) if order == "max" else min(prev)

N = int(input())

matrix = []

for i in range(N):
    matrix.append(list(map(int, input().split())))

max_num = solution(N, matrix, "max")
min_num = solution(N, matrix, "min")
print(max_num, min_num)