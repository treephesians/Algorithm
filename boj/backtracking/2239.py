import sys
input = sys.stdin.readline

sdoku = [list(map(int, list(input().strip()))) for _ in range(9)]

def is_valid(r, c, num):
    # 행 검사
    for i in range(9):
        if sdoku[r][i] == num:
            return False
    # 열 검사
    for i in range(9):
        if sdoku[i][c] == num:
            return False
    # 3x3 박스 검사
    br = (r // 3) * 3
    bc = (c // 3) * 3
    for i in range(br, br+3):
        for j in range(bc, bc+3):
            if sdoku[i][j] == num:
                return False
    return True

def backtracking(row, col):
    # 마지막 열을 넘어가면 다음 행으로 이동
    if col == 9:
        return backtracking(row+1, 0)
    # 마지막 행까지 채웠다면 스도쿠 완성
    if row == 9:
        for line in sdoku:
            print("".join(map(str, line)))
        sys.exit(0)  # 프로그램 종료
    
    if sdoku[row][col] == 0:
        for num in range(1, 10):
            if is_valid(row, col, num):
                sdoku[row][col] = num
                if backtracking(row, col+1):
                    return True
                sdoku[row][col] = 0
        return False
    else:
        return backtracking(row, col+1)

backtracking(0, 0)


# backtracking 할 때에는 어디서 추가할지 (뺄지)와
# 그 position을 정확히 정하는 것이 좋다.