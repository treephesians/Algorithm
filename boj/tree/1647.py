import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())

priority_queue = []
parents = [i for i in range(N + 1)]
rank = [0 for _ in range(N + 1)]

def find(parents, n):
    if parents[n] == n:
        return n
    return find(parents, parents[n])

def union(a, b):
    a = find(parents, a)
    b = find(parents, b)
    if rank[a] == rank[b]:
        parents[a] = b
        rank[b] += 1
    elif rank[a] > rank [b]:
        parents[b] = a
        rank[a] += rank[b]
    else:
        parents[a] = b
        rank[b] += rank[a]
        

for _ in range(M):
    A, B, C = map(int, input().split())
    heapq.heappush(priority_queue, (C, A, B))

result = []

while priority_queue:
    C, A, B = heapq.heappop(priority_queue)
    if find(parents, A) != find(parents, B):
        result.append(C)
        union(A, B)

print(sum(result[0:-1]))