import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

matrix = [[] for _ in range(N + 1)]
degree = [0 for _ in range(N + 1)]
q = deque([])
result = []

for _ in range(M):
    arr = list(map(int, input().split()))
    for i in range(1, arr[0]):
        matrix[arr[i]].append(arr[i + 1])
        degree[arr[i + 1]] += 1

for i in range(1, N + 1):
    if degree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    result.append(now)
    for next in matrix[now]:
        degree[next] -= 1
        if degree[next] == 0:
            q.append(next)

if len(result) == N:
    for i in result:
        print(i)
else:
    print(0)