import sys
import heapq

INF = int(1e9)
V, E = map(int, sys.stdin.readline().split())
start_v = int(sys.stdin.readline())

graph = [[] for _ in range(V + 1)]
distance = [INF for _ in range(V + 1)] # 거리 테이블용
visited = [False for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

def dijkstra(start_v):
    
    queue = []
    heapq.heappush(queue, (0, start_v))
    distance[start_v] = 0
    visited[start_v] = True

    while queue:
        now_w, now_v = heapq.heappop(queue)
        
        for next_v, next_w in graph[now_v]:
            cost = now_w + next_w
            if distance[next_v] > cost:
                distance[next_v] = cost
                heapq.heappush(queue, (cost, next_v))

dijkstra(start_v)

for i in range(1, V + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
                

            
    