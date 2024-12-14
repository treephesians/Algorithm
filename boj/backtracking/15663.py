# https://www.acmicpc.net/problem/15663
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

result = []
visited = [False for _ in range(N)]

def backtracking(n):
    result.append(arr[n])
    visited[n] = True
    if len(result) == M:
        print(" ".join(map(str, result)))
        result.pop()
        visited[n] = False
        return
    before = 0
    for i in range(N):
        if not visited[i] and arr[i] != before:
            backtracking(i)
            before = arr[i]
    result.pop()    
    visited[n] = False

for i in range(N):
    if i >= 1 and arr[i] == arr[i - 1]:
        continue
    backtracking(i)