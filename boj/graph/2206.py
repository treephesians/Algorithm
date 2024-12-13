# https://www.acmicpc.net/problem/2206

import sys
from collections import deque

input = sys.stdin.readline

row, col = map(int, input().split())
matrix = []

for _ in range(row):
    matrix.append(list(input().strip()))

queue = deque() # row, col, distance, broken
queue.append((0, 0, 1, 0))
visited = [[[False] * 2 for _ in range(col)] for _ in range(row)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
success = False

while queue:
    r, c, dist, broken = queue.popleft()
    visited[r][c][broken] = True
    if r == row - 1 and c == col - 1:
        print(dist)
        success = True
        break
    for i in range(4):
        next_row = r + dy[i]
        next_col = c + dx[i]
        if 0 <= next_col < col and 0 <= next_row < row:
            if not visited[next_row][next_col][broken]:
                if matrix[next_row][next_col] == '0':
                    queue.append((next_row, next_col, dist + 1, broken))
                    visited[next_row][next_col][broken] = True
                elif not broken:
                    queue.append((next_row, next_col, dist + 1, 1))
                    visited[next_row][next_col][broken] = True

if not success:
    print(-1)