from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    q = deque([[0, 0, 1]])
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    while q:
        now = q.popleft()
        y = now[0]
        x = now[1]
        length = now[2]
        if x == m-1 and y == n-1:
            return length
        
        if not visited[y][x]:
            visited[y][x] = True
            if y + 1 < n and maps[y + 1][x] and not visited[y + 1][x]:
                q.append([y + 1, x, length + 1])
            if y - 1 >= 0 and maps[y - 1][x] and not visited[y - 1][x]:
                q.append([y - 1, x, length + 1])
            if x + 1 < m and maps[y][x + 1] and not visited[y][x + 1]:
                q.append([y, x + 1, length + 1])
            if x - 1 >= 0 and maps[y][x - 1] and not visited[y][x - 1]:
                q.append([y, x - 1, length + 1])
                
    return -1

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1], [1,1,1,1,1]] # answer = 11
#maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]] # answer = -1
#maps = [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]] # answer = 11
print(solution(maps))