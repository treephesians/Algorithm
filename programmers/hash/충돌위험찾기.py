from collections import defaultdict

def solution(points, routes):
    pos_points = {i + 1: point for i, point in enumerate(points)}
    timedict = defaultdict(int)
    
    for route in routes:
        time = 0
        len_route = len(route)
        r, c = pos_points[route[0]]
        timedict[(time, r, c)] += 1

        for i in range(1, len_route):
            nr, nc = pos_points[route[i]]
            while r != nr:
                r += 1 if r < nr else -1
                time += 1
                timedict[(time, r, c)] += 1

            while c != nc:
                c += 1 if c < nc else -1
                time += 1
                timedict[(time, r, c)] += 1

    danger = sum(1 for cnt in timedict.values() if cnt >= 2)
    
    return danger

points = [[3, 2], [6, 4], [4, 7], [1, 4]]
routes = [[4, 2], [1, 3], [2, 4]]
print(solution(points, routes))
