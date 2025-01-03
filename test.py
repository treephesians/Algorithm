import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
result = [0 for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque([1])

while q:
    now = q.popleft()
    if not visited[now]:
        visited[now] = True
        for next in graph[now]:
            if not visited[next]:
                result[next] = now
                q.append(next)

for i in range(2, N + 1):
    print(result[i])

