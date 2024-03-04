def solution(n, m, x, y, queries):
    def simulate_query(start_x, start_y, dx, dy):
        current_x, current_y = start_x, start_y
        while True:
            current_x += dx
            current_y += dy
            if current_x < 0 or current_x >= n or current_y < 0 or current_y >= m:
                break
        return current_x, current_y

    count = 0
    for i in range(n):
        for j in range(m):
            current_x, current_y = i, j
            for query in queries:
                direction, distance = query
                if direction == 0:
                    current_y -= distance
                elif direction == 1:
                    current_y += distance
                elif direction == 2:
                    current_x -= distance
                elif direction == 3:
                    current_x += distance
                current_x = max(0, min(current_x, n - 1))
                current_y = max(0, min(current_y, m - 1))

            if current_x == x and current_y == y:
                count += 1

    return count

# 예시 테스트
print(solution(2, 2, 0, 0, [[2,1],[0,1],[1,1],[0,1],[2,1]]))  # 기대 출력: 4
print(solution(2, 5, 0, 1, [[3,1],[2,2],[1,1],[2,3],[0,1],[2,1]]))  # 기대 출력: 2
