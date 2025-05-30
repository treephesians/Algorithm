import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def bfs(start_i, start_j, grid, visited, N):
    """Breadth‐first search to mark all cells in the same region."""
    q = deque([(start_i, start_j)])
    visited[start_i][start_j] = True
    color = grid[start_i][start_j]
    # 4 방향: 상, 하, 좌, 우
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and grid[nx][ny] == color:
                    visited[nx][ny] = True
                    q.append((nx, ny))

def count_regions(grid, N):
    """Count connected regions in the given grid."""
    visited = [[False]*N for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                bfs(i, j, grid, visited, N)
                count += 1
    return count

def main():
    N = int(input())
    # 원본 그림
    grid_normal = [list(input()) for _ in range(N)]
    # 적록색약용 그림: G를 R로 치환
    grid_colorblind = [
        ['R' if c == 'G' else c for c in row]
        for row in grid_normal
    ]

    normal_count = count_regions(grid_normal, N)
    colorblind_count = count_regions(grid_colorblind, N)
    print(normal_count, colorblind_count)

if __name__ == "__main__":
    main()