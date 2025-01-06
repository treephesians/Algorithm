import sys

input = sys.stdin.readline

N, M = map(int, input().split())

arr = []
def backtracking(n):
    arr.append(n)
    if len(arr) == M:
        print(*arr)
    else:
        for i in range(n + 1, N + 1):
            backtracking(i)
    arr.pop()

for i in range(1, N + 1):
    backtracking(i)