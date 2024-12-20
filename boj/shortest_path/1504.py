import sys
import heapq

input = sys.stdin.readline
max_length = int(1e9)

N, E = map(int, input().split())

graph = [[] for _ in range(N + 1)]


for _ in range(E):
    v1, v2 ,cost = map(int, input().split())
    graph[v1].append((v2, cost))
    graph[v2].append((v1, cost))

v1, v2 = map(int, input().split())

def dijkstra(start, end):
    visited = [False for _ in range(N + 1)]
    distance = [max_length for _ in range(N + 1)]
    hq = []
    distance[start] = 0
    heapq.heappush(hq, (0, start))
    while hq:
        d, v = heapq.heappop(hq)
        if visited[v]:
            continue
        visited[v] = True
        for nv, nd in graph[v]:
            if d + nd < distance[nv]:
                distance[nv] = d + nd
                if not visited[nv]:
                    heapq.heappush(hq, (d+ nd, nv))
    return distance[end]


answer = min(dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N), dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N))
if answer >= max_length:
    print(-1)
else: print(answer)
