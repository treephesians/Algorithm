import sys
from collections import deque

def find_start(_matrix, _row, _col):
    arr = deque()
    zeros = 0
    for r in range(_row):
        for c in range(_col):
            if _matrix[r][c] == 1:
                arr.append([r, c, 0])
            elif _matrix[r][c] == 0:
                zeros += 1
    return arr, zeros

def BFS_UDLR(queue, _matrix, _row, _col, zeros):
    day = 0
    while queue:
        r, c, day = queue.popleft()
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < _row and 0 <= nc < _col and _matrix[nr][nc] == 0:
                _matrix[nr][nc] = 1
                queue.append((nr, nc, day + 1))
                zeros -= 1
    return day if zeros == 0 else -1

col, row = map(int, sys.stdin.readline().split())
matrix = []
visited = [[False for _ in range(col)] for _ in range(row)]

for _ in range(row):
    matrix.append(list(map(int, sys.stdin.readline().split())))

start_arr, zeros = find_start(matrix, row, col)

result = BFS_UDLR(start_arr, matrix, row, col, zeros)

print(result)