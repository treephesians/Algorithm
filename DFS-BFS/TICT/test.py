from collections import deque

def make_matrix():
    n, m, v = map(int, input().split())
    matrix = [[0 for _ in range(n+1)] for _ in range(n+1)] # [[0] * (n+1)] * (n+1) 을 하면 안된다! 주소가 공유되기 때문이다.
    for _ in range(m):
        f, t = map(int, input().split())
        matrix[f][t] = matrix[t][f] = 1
    return n, matrix, v

def dfs_matrix_recursion(n, matrix, point, visited):
    if not visited[point]:
        print(point, end=" ")
        visited[point] = True
    for i in range(1, n + 1):
        if matrix[point][i] == 1 and not visited[i]:
            dfs_matrix_recursion(n, matrix, i, visited)
            
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

n, matrix, start = make_matrix()
visited = [False] * (n+1)
dfs_matrix_recursion(n, matrix, start, visited)
visited = [False] * (n+1)
print()
bfs_with_matrix(n, matrix, start, visited)