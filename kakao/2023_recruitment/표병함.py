from collections import defaultdict, deque


def solution(commands):
    answer = []
    table = [['' for _ in range(50)] for _ in range(50)]
    dd = defaultdict(list)

    for command in commands:

        arr = command.split(" ")

        if arr[0] == "UPDATE" and len(arr) == 4:
            r = int(arr[1]) - 1
            c = int(arr[2]) - 1
            visited = [[False for _ in range(50)] for _ in range(50)]
            dq = deque([(r, c)])
            while dq:
                r, c = dq.popleft()
                if visited[r][c]:
                    continue
                visited[r][c] = True
                table[r][c] = arr[3]
                for nr, nc in dd[(r, c)]:
                    if not visited[nr][nc]:
                        dq.append((nr, nc))

        if arr[0] == "UPDATE" and len(arr) == 3:
            for i in range(50):
                for j in range(50):
                    if table[i][j] == arr[1]:
                        table[i][j] = arr[2]

        if arr[0] == "MERGE":
            cell1 = (int(arr[1]) - 1, int(arr[2]) - 1)
            cell2 = (int(arr[3]) - 1, int(arr[4]) - 1)
            dd[cell1].append(cell2)
            dd[cell2].append(cell1)

        if arr[0] == "UNMERGE":
            r = int(arr[1]) - 1
            c = int(arr[2]) - 1
            visited = [[False for _ in range(50)] for _ in range(50)]
            dq = deque([(r, c)])
            while dq:
                r, c = dq.popleft()
                if visited[r][c]:
                    continue
                visited[r][c] = True
                temp = dd[(r, c)]
                dd[(r, c)] = []
                for nr, nc in temp:
                    if not visited[nr][nc]:
                        dq.append((nr, nc))
        
        if arr[0] == "PRINT":
            result = table[int(arr[1]) - 1][int(arr[2]) - 1] if table[int(arr[1]) - 1][int(arr[2]) - 1] != '' else "EMPTY"
            answer.append(result)
        
    return answer

print(solution(["MERGE 1 2 1 3", "UPDATE 1 2 menu"]))