# BFS
# 인접행렬 + deqeue
# 인접리스트 + deque
from collections import deque

def make_matrix():
    n, m, v = map(int, input().split())
    matrix = [[0 for _ in range(n+1)] for _ in range(n+1)] # [[0] * (n+1)] * (n+1) 을 하면 안된다! 주소가 공유되기 때문이다.
    for _ in range(m):
        f, t = map(int, input().split())
        matrix[f][t] = matrix[t][f] = 1
    return n, matrix, v

def make_list():
    n, m, v = map(int, input().split())
    mlist = [[] for _ in range(n + 1)]
    for _ in range(m):
        f, t = map(int, input().split())
        mlist[f].append(t)
        mlist[f].sort()
        mlist[t].append(f)
        mlist[t].sort()
    return n, mlist, v

def bfs_with_matrix(n, matrix, start, visited):
    queue = deque([start])
    while queue:
        now = queue.popleft()
        if not visited[now]:
            print(now, end=" ")
            visited[now] = True
        for i in range(1, n+1):
            if matrix[now][i] == 1 and not visited[i]:
                queue.append(i)
    return None

def bfs_with_list(mlist, start, visited):
    queue = deque([start])
    while queue:
        now = queue.popleft()
        if not visited[now]:
            print(now, end=" ")
            visited[now] = True
        for i in mlist[now]:
            if not visited[i]:
                queue.append(i)

#n, matrix, start = make_matrix()
#visited = [False] * (n+1)
#bfs_with_matrix(n, matrix, start, visited)
n, mlist, start = make_list()
visited = [False] * (n+1)
bfs_with_list(mlist, start, visited)