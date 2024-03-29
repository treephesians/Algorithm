import sys

N, M = map(int, sys.stdin.readline().split())

vertices = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
stack = []

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    vertices[u].append(v)
    vertices[v].append(u)

connected_component = 0

for i in range(1, N + 1):
    if not visited[i]:
        stack = [i]
        visited[i] = True
        connected_component += 1
        
        while stack:
            now = stack.pop()
            for next_node in vertices[now]:
                if not visited[next_node]:
                    stack.append(next_node)
                    visited[next_node] = True
    
print(connected_component)