# DFS

# 1. 인접행렬 + stack
# 2. 인접행렬 + 재귀
# 3. 인접리스트 + stack
# 4. 인접리스트 + 재귀

def make_matrix():
    n, m, v = map(int, input().split())
    matrix = [[0 for _ in range(n+1)] for _ in range(n+1)] # [[0] * (n+1)] * (n+1) 을 하면 안된다! 주소가 공유되기 때문이다.
    for _ in range(m):
        f, t = map(int, input().split())
        matrix[f][t] = matrix[t][f] = 1
    return n, matrix, v

def dfs_matrix_stack(n, matrix, start, visited):
    stack = [start]
    
    while stack:
        point = stack.pop()
        if not visited[point]:
            print(point, end=" ")
        visited[point] = True
        for i in range(n, -1, -1):
            if matrix[point][i] == 1 and visited[i] == False:
                stack.append(i)
    return None

def dfs_matrix_recursion(n, matrix, point, visited):
    if not visited[point]:
        print(point, end=" ")
        visited[point] = True
    for i in range(1, n + 1):
        if matrix[point][i] == 1 and not visited[i]:
            dfs_matrix_recursion(n, matrix, i, visited)
    
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

def dfs_list_stack(mlist, start, visited):
    stack = [start]
    while stack:
        now = stack.pop()
        if not visited[now]:
            print(now, end=" ")
            visited[now] = True
        for i in range(len(mlist[now])-1, -1, -1):
            next = mlist[now][i]
            if not visited[next]:
                stack.append(next)
 
    return None

def dfs_list_recursion(mlist, point, visited):
    if not visited[point]:
        print(point, end=" ")
        visited[point] = True
    for i in mlist[point]:
        if not visited[i]:
            dfs_list_recursion(mlist, i, visited)


### Test Code ###
#n, matrix, start = make_matrix()
# visited = [False] * (n+1)
# dfs_matrix_stac(n, matrix, start, visited)
# dfs_matrix_recursion(n, matrix, start, visited)

# n, mlist, start = make_list()
# visited = [False] * (n+1)
# dfs_list_stack(mlist, start, visited)
# dfs_list_recursion(mlist, start, visited)
        
    