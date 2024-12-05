import sys

input = sys.stdin.readline

N, M = map(int, input().split())

def dfs(n, arr):
    arr.append(n)
    if len(arr) == M:
        print(' '.join(map(str,arr)))
    else:
        for i in range(n + 1, N + 1):
            dfs(i, arr)
            arr.pop()

for i in range(1, N+1):
    dfs(i,[])