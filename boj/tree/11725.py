# https://www.acmicpc.net/problem/11725
import sys

input = sys.stdin.readline

N = int(input())
visited = [False] * (N + 1)
parents = [0] * (N + 1)
queue = [1]
matrix = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    v1, v2 = map(int, input().split())
    matrix[v1].append(v2)
    matrix[v2].append(v1)

while queue:
    now = queue.pop()
    if not visited[now]:
        visited[now] = True
        for next in matrix[now]:
            if not visited[next]:
                parents[next] = now
                queue.append(next)

for i in range(2, N + 1):
    print(parents[i])

