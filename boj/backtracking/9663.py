# https://www.acmicpc.net/problem/9663

import sys
input = sys.stdin.readline

N = int(input())

result = 0
cols = set()           # 열에 퀸이 있는지 관리
pos_diagonal = set()   # (r+c)가 같은 대각선 관리
neg_diagonal = set()   # (r-c)가 같은 대각선 관리

def backtrack(row):
    global result
    if row == N:
        result += 1
        return
    
    for col in range(N):
        # 충돌 체크
        if col in cols or (row+col) in pos_diagonal or (row-col) in neg_diagonal:
            continue
        
        # 현재 위치에 퀸을 배치
        cols.add(col)
        pos_diagonal.add(row+col)
        neg_diagonal.add(row-col)
        
        # 다음 행으로
        backtrack(row+1)
        
        # 백트래킹(원상복귀)
        cols.remove(col)
        pos_diagonal.remove(row+col)
        neg_diagonal.remove(row-col)

backtrack(0)
print(result)

