# https://www.acmicpc.net/problem/1987

import sys

input = sys.stdin.readline

R, C = map(int, input().split())

arr = []
for r in range(R):
    arr.append([c for c in input().strip()])

visited = set()
max_count = 0
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def backtracking(row, col, count):
    global max_count
    max_count = max(count, max_count)
    visited.add(arr[row][col])
    for i in range(4):
        nr = row + dr[i]
        nc = col + dc[i]
        if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] not in visited:
            backtracking(nr, nc, count + 1)
    visited.remove(arr[row][col])

backtracking(0, 0, 1)
print(max_count)