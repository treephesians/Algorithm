# https://www.acmicpc.net/problem/11660
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for row in range(1, N + 1):
    col = 1
    for n in list(map(int, input().split())):
        matrix[row][col] = n + matrix[row - 1][col] + matrix[row][col - 1] - matrix[row - 1][col - 1]
        col += 1

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(matrix[x2][y2] - matrix[x2][y1 - 1] - matrix[x1 - 1][y2] + matrix[x1 - 1][y1 - 1])