import sys
from collections import deque

input = sys.stdin.readline

def is_all_done(cube, M, N, H):
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if cube[h][n][m] == 0:
                    return False
    return True

def solution(cube, tc, M, N, H):
    result = 0

    if is_all_done(cube, M, N, H):
        return result
    
    dq = deque(tc)

    dm = [1, -1, 0, 0, 0, 0]
    dn = [0, 0, 1, -1, 0, 0]
    dh = [0, 0, 0, 0, 1, -1]

    while dq:
        m, n, h, day = dq.popleft()
        result = max(result, day)
        for i in range(6):
            nm = m + dm[i]
            nn = n + dn[i]
            nh = h + dh[i]
            if 0 <= nm < M and 0 <= nn < N and 0 <= nh < H and cube[nh][nn][nm] == 0:
                cube[nh][nn][nm] = 1
                dq.append([nm, nn, nh, day + 1])
    
    if is_all_done(cube, M, N, H):
        return result
    else:
        return -1

# col, row, height
M, N, H = map(int, input().split())

cube = [[0 for _ in range(N)] for _ in range(H)]
tomatoes_coords = []

for h in range(H):
    for n in range(N):
        arr = list(map(int, input().split()))
        for m in range(len(arr)):
            if arr[m] == 1:
                tomatoes_coords.append([m, n, h, 0])
        cube[h][n] = arr

print(solution(cube, tomatoes_coords, M, N, H))