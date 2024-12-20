import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
dist = [INF for _ in range(N + 1)]
hq = []
for _ in range(M):
    city1, city2, cost = map(int, input().split())
    graph[city1].append([city2, cost])

start, end = map(int, input().split())
dist[start] = 0
heapq.heappush(hq, (dist[start], start))

while hq:
    d, v = heapq.heappop(hq)
    if visited[v]:
        continue
    visited[v] = True
    for nv, nd in graph[v]:
        if dist[nv] > d + nd:
            dist[nv] = d + nd
            if not visited[nv]:
                heapq.heappush(hq, (dist[nv], nv))

print(dist[end])
