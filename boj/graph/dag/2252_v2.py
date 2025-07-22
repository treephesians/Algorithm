import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N)]
visited = [False for _ in range(N)]

for i in range(M):
    A, B = map(int, input().split())
    graph[B - 1].append(A - 1)

for i in range(N):
    if not visited[i]:
        stack = [i]
        while stack:
            now = stack.pop()
            visited[now] = True
            for next in graph[now]:
                if not visited[next]:
                    stack.append(next)


