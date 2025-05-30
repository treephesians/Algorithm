import sys

input = sys.stdin.readline
row, col = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(row)]
visited = [[False for _ in range(col)] for _ in range(row)]
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

answer = 0

def dfs(n, tr, tc, result):
    global answer

    if n == 4:
        answer = max(answer, result)
        return
    
    visited[tr][tc] = True 

    
    for i in range(4):
        [nr, nc] = [tr + dirs[i][0], tc + dirs[i][1]]
        if 0 <= nr < row and 0 <= nc < col and not visited[nr][nc]:
            dfs(n + 1, nr, nc, result + matrix[nr][nc])
    
    visited[tr][tc] = False

# 이 부분이 킥인 것 같다..!!
def check_t_shape(x, y):
    """‘ㅗ’ 모양 테트로미노 처리: 
       (x,y)를 중심으로 네 방향 중 임의의 세 방향을 골라 합산"""
    global answer
    wings = []
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < row and 0 <= ny < col:
            wings.append(matrix[nx][ny])
    if len(wings) < 3:
        return
    # 가장 큰 세 날개를 선택
    wings.sort(reverse=True)
    s = matrix[x][y] + wings[0] + wings[1] + wings[2]
    answer = max(answer, s)
    
for r in range(row):
    for c in range(col):
        dfs(1, r, c, matrix[r][c])
        check_t_shape(r, c)

print(answer)
