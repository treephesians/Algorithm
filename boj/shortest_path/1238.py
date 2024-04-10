import sys
import heapq

INF = int(1e9)
N, M, X = map(int, sys.stdin.readline().split())

graph = [ [] for _ in range(N + 1) ]


for _ in range(M):
     start, end, time = map(int, sys.stdin.readline().split())
     graph[start].append((end, time))
     
def dijkstras(start):
     
     queue = []
     heapq.heappush(queue, (0, start))
     distance = [ INF for _ in range(N + 1) ]
     distance[start] = 0
     
     while queue:
          now_time, now_v = heapq.heappop(queue)
          for next_v, next_time in graph[now_v]:
               cost = now_time + next_time
               if distance[next_v] > cost:
                    distance[next_v] = cost
                    heapq.heappush(queue, (cost, next_v))
     
     return distance

from_N_to_X = [0 for _ in range(N + 1)]

from_X_to_N = dijkstras(X)

for i in range(1, N + 1):
     from_N_to_X[i] = dijkstras(i)[X]

res = 0
for i in range(1, N + 1):
     cost = from_N_to_X[i] + from_X_to_N[i]
     if cost > res:
          res = cost

print(res)