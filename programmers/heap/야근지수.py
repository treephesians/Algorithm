import heapq

def solution(n, works):
    answer = 0
    works = [-w for w in works]
    heapq.heapify(works)

    for i in range(n):
        m = heapq.heappop(works)
        if m == 0:
            break
        heapq.heappush(works, m + 1)

    return sum(w ** 2 for w in works)

print(solution(4, [4, 3, 3]))