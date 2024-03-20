import sys

n_computers = int(sys.stdin.readline())
n_lines = int(sys.stdin.readline())

graph = [[] for _ in range(n_computers + 1)]
visited = [False]  * (n_computers + 1)
for _ in range(n_lines):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

queue = [1]
while queue:
    now = queue.pop(0)
    visited[now] = True
    for next in graph[now]:
        if not visited[next]:
            queue.append(next)
    
result = len([x for x in visited if x]) - 1
print(result)