import sys

input = sys.stdin.readline

V, E = map(int, input().split())

hq = []
parent = [0 for _ in range(V + 1)]
rank = [0 for _ in range(V + 1)]

for i in range(1, V + 1):
    parent[i] = i

for _ in range(E):
    v1, v2, cost = map(int, input().split())
    hq.append([cost, v1, v2])

def find_parent(parent, x):
    p = parent[x]
    if p != x:
        return find_parent(parent, p)
    return p

def union(a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if rank[a] < rank[b]:
        parent[a] = b
        rank[a] += rank[b]
    elif rank[a] > rank[b]:
        parent[b] = a
    else:
        parent[a] = b
        rank[b] += 1

hq.sort()
result = 0
for i in range(E):
    cost, v1, v2 = hq[i]
    if find_parent(parent, v1) == find_parent(parent, v2):
        continue
    result += cost
    union(v1, v2)

print(result)