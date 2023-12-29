def solution(sizes):
    
    w = 0
    h = 0
    
    for size in sizes:
        size.sort()
    
    for size in sizes:
        w = max(w, size[0])
        h = max(h, size[1])
    
    return w * h

sizes = [[50, 60], [30, 70], [30, 60], [40, 80]]
sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
sizes = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
print(solution(sizes))