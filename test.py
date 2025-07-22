import sys

input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
arr = [0] * (N + 1)

for _ in range(N - 1):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

def DFS_stack(start):
    stack = [start]
    visited[start] = True

    while stack:
        parent = stack.pop()
        for child in graph[parent]:
            if not visited[child]:
                visited[child] = True
                arr[child] = parent
                stack.append(child)

DFS_stack(1)

for i in range(2, N + 1):
    print(arr[i])