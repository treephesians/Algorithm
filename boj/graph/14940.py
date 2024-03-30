import sys
from collections import deque

row, col = map(int, sys.stdin.readline().split())

matrix = []
queue = deque([])
visited = [[False for _ in range(col)] for _ in range(row)]

count = 0
for r in range(row):
    arr = list(map(int, sys.stdin.readline().split()))
    matrix.append(arr)
    if 2 in arr:
        for c in range(col):
            if arr[c] == 2:
                queue.append([r, c, 0])
                visited[r][c] = True
                matrix[r][c] = 0

while queue:
    r, c, length = queue.popleft()
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    for i in range(4):
        next_r = r + dr[i]
        next_c = c + dc[i]
        if 0 <= next_r < row and 0 <= next_c < col and matrix[next_r][next_c] == 1 and not visited[next_r][next_c]:
            queue.append([next_r, next_c, length + 1])
            visited[next_r][next_c] = True
            matrix[next_r][next_c] = length + 1
            
for r in range(row):
    for c in range(col):
        if not visited[r][c] and matrix[r][c]:
            matrix[r][c] = -1
        print(matrix[r][c], end=" ")
    print()